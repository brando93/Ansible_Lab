# Ansible Docker Lab (Local Practice on macOS)

This document describes the **exact steps followed** to build a simple and reproducible **local Ansible lab using Docker and Docker Compose** on macOS.

The Purpose: of this lab is to practice Ansible fundamentals using containers instead of virtual machines.

---

## Lab Goals

- Practice Ansible basics locally
- Use **SSH key-based authentication**
- Avoid manual SSH setup on every run
- Use Docker containers as:
  - **Ansible control node**
  - **Managed nodes**

---

## 1. Prerequisites

- macOS
- Docker Desktop installed and running
- Docker Compose (included with Docker Desktop)
- Basic terminal knowledge

Verify Docker is working:

```bash
docker version
docker compose version
```

2. Project Structure Creation

Create the project directory and file structure:


```bash
cd ~/Desktop

mkdir -p ansible-lab/{ansible,control,jenkins,node}

touch ansible-lab/docker-compose.yml
touch ansible-lab/README.md

touch ansible-lab/ansible/{ansible.cfg,inventory}
touch ansible-lab/ansible/playbooks/deploy_apache.yml

touch ansible-lab/control/Dockerfile
touch ansible-lab/node/Dockerfile

touch ansible-lab/jenkins/{Dockerfile,Jenkinsfile}
```

Generate an SSH key pair for Ansible:

```bash
ssh-keygen -t ed25519 -f ansible-lab/control/id_ed25519 -N ""
```

This creates:

id_ed25519 (private key)
id_ed25519.pub (public key)

Final directory structure:

```bash
.
├── ansible
│   ├── ansible.cfg
│   ├── inventory
│   ├── playbooks
│   │   └── deploy_apache.yml
│   └── roles
│       └── apache_role
│           ├── handlers
│           │   └── main.yml
│           ├── README.md
│           ├── tasks
│           │   └── main.yml
│           ├── templates
│           │   ├── index.html.j2
│           │   └── motd.j2
│           └── vars
│               └── main.yml
├── control
│   ├── Dockerfile
│   ├── id_ed25519
│   ├── id_ed25519.pub
│   └── node
│       └── authorized_keys
├── docker-compose.yml
├── jenkins
│   ├── Dockerfile
│   └── Jenkinsfile
├── node
│   ├── authorized_keys
│   └── Dockerfile
└── README.md

13 directories, 19 files
```



3. Prepare SSH Access for Managed Nodes

Copy the public key into authorized_keys:

```bash
cat control/id_ed25519.pub > node/authorized_keys
cp node/authorized_keys control/node/authorized_keys
```

Purpose::

Allows the control node to SSH into managed nodes
Ensures key-based auth is baked into images
Avoids reconfiguring keys every time containers restart


4. Control Node Dockerfile

File: control/Dockerfile

```bash
FROM quay.io/ansible/ansible-runner:latest

USER root

RUN mkdir -p /root/.ssh
COPY id_ed25519 /root/.ssh/id_ed25519
COPY id_ed25519.pub /root/.ssh/id_ed25519.pub

RUN chmod 600 /root/.ssh/id_ed25519 && \
    chmod 644 /root/.ssh/id_ed25519.pub

WORKDIR /ansible
CMD ["sleep", "infinity"]
```

Purpose:

Uses the official Ansible Runner image
Installs SSH keys for outbound connections
Sets /ansible as working directory for playbooks


5. Managed Node Dockerfile

File: node/Dockerfile

```bash
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo && \
    mkdir /var/run/sshd

RUN useradd -m ansible && \
    echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN mkdir -p /home/ansible/.ssh
COPY authorized_keys /home/ansible/.ssh/authorized_keys

RUN chown -R ansible:ansible /home/ansible/.ssh && \
    chmod 700 /home/ansible/.ssh && \
    chmod 600 /home/ansible/.ssh/authorized_keys

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
```

Purpose:

Creates an SSH-enabled Ubuntu node
Adds an ansible user with passwordless sudo
Installs Python (required by Ansible)
Allows SSH access using keys only


6. Jenkins Dockerfile

File: Dockerfile

```bash
FROM jenkins/jenkins:lts

USER root

# Necesario para docker exec
RUN apt-get update && \
    apt-get install -y docker.io ssh && \
    rm -rf /var/lib/apt/lists/*

USER jenkins
```

File: Jenkinsfile

```bash
pipeline {
  agent any

  stages {

    stage('Check environment') {
      steps {
        echo 'Checking containers...'
        sh 'docker ps'
      }
    }

    stage('Run Ansible Playbook') {
      steps {
        echo 'Deploying Apache using Ansible'
        sh '''
          docker exec ansible-control \
          ansible-playbook ansible/ansible/playbooks/deploy_apache.yml
        '''
      }
    }

  }
}
```


7. Docker Compose Configuration

File: docker-compose.yml

```bash
services:
  ansible-control:
    build: ./control
    container_name: ansible-control
    volumes:
      - .:/ansible

  node1:
    build: ./node
    container_name: node1

  node2:
    build: ./node
    container_name: node2

  jenkins:
    build: ./jenkins
    image: jenkins/jenkins:lts
    container_name: jenkins
    user: root
    ports:
      - "8080:8080"
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock

volumes:
  jenkins_home:
```

Purpose:

Builds both images locally
Mounts Ansible files into the control node
Creates an isolated Docker network automatically


8. Ansible Inventory

File: ansible/inventory

```bash
[node]
node1 ansible_user=ansible ansible_host=node1
node2 ansible_user=ansible ansible_host=node2
```

Purpose:

Defines managed hosts
Uses Docker service name as hostname
Uses the ansible user created in the node container

9. Ansible Playbook

File: ansible/playbook.yml

```bash
- hosts: node
  become: true
  tasks:
    - name: Ensure curl is installed
      apt:
        name: curl
        state: present
        update_cache: true
```

Purpose:

Simple validation playbook
Tests SSH connectivity
Tests privilege escalation
Tests package management

10. Build and Start the Lab

From the project root:

> docker compose up -d --build


This:

Builds both images
Starts the containers
Keeps SSH keys persistent inside images

11. Access the Control Node

> docker exec -it ansible-control bash


Inside the container, verify connectivity:

> ansible all -i inventory -m ping

Now on your local open localhost browser

> http://localhost:8080

Paste output from jenkins container

> docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

Configure Jenkins:

- Set default plugins config
- Skip admin user config
- Instance configuration Save and Finsh
- Create Job > Pipeline
- Scroll to Pipeline > Definition > Pipeline script
- Paste jenkinsfile in script area
- Apply + Save

12. Down the environment but keep it ready for next time

> docker compose down

13. Stop and Remove the Lab completely

> docker compose down -v
> docker compose down --remove-orphans
> docker system prune -a --volumes


This removes:

Containers
Docker network
Volumes created by Compose


⚠️ Warning: This removes all unused Docker resources (containers, images, volumes, networks).


14. Start the lab again where you left it

> docker compose up -d