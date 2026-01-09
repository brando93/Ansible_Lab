# 🚀 Ansible Lab - CI/CD Pipeline with Jenkins & FastAPI

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=flat&logo=ansible&logoColor=white)](https://www.ansible.com/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white)](https://www.jenkins.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

> **Complete CI/CD infrastructure lab** using Docker, Ansible, Jenkins, and FastAPI with AI capabilities. Perfect for learning DevOps practices locally on macOS.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Components](#-components)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

---

## 🎯 Overview

This project demonstrates a **complete DevOps pipeline** running entirely in Docker containers:

- **Jenkins** orchestrates CI/CD workflows
- **Ansible** manages infrastructure as code
- **FastAPI** provides a production-ready AI-powered REST API
- **Docker** containerizes everything for portability

Perfect for:
- 🎓 Learning DevOps practices
- 🧪 Testing Ansible playbooks locally
- 🚀 Prototyping CI/CD pipelines
- 🤖 Experimenting with AI APIs

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          HOST MACHINE (macOS)                        │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    Docker Environment                        │   │
│  │                                                               │   │
│  │  ┌──────────────┐         ┌─────────────────────────────┐  │   │
│  │  │   Jenkins    │         │   Ansible Control Node      │  │   │
│  │  │   :8080      │────────▶│   - Ansible Core            │  │   │
│  │  │              │  Exec   │   - Python 3                │  │   │
│  │  │  - Pipeline  │         │   - SSH Keys                │  │   │
│  │  │  - Jobs      │         │   - Docker CLI              │  │   │
│  │  └──────┬───────┘         └────────┬────────────────────┘  │   │
│  │         │                          │                        │   │
│  │         │                          │ SSH                    │   │
│  │         │                          ▼                        │   │
│  │         │         ┌────────────────────────────────┐       │   │
│  │         │         │   ansible-lab_ansible-net      │       │   │
│  │         │         │   (Docker Network)             │       │   │
│  │         │         └────────────────────────────────┘       │   │
│  │         │                          │                        │   │
│  │         │         ┌────────────────┴────────────────┐      │   │
│  │         │         │                                  │      │   │
│  │         │    ┌────▼─────┐                    ┌──────▼────┐ │   │
│  │         │    │   DEV    │                    │   PROD    │ │   │
│  │         │    │  Node    │                    │   Node    │ │   │
│  │         │    │          │                    │           │ │   │
│  │         │    │ ┌──────┐ │                    │ ┌───────┐ │ │   │
│  │         │    │ │FastAPI│ │                    │ │FastAPI│ │ │   │
│  │         └───▶│ │:8001 │ │                    │ │:8002  │ │ │   │
│  │   HTTP       │ │      │ │                    │ │       │ │ │   │
│  │              │ │Mock  │ │                    │ │Full AI│ │ │   │
│  │              │ │Mode  │ │                    │ │Model  │ │ │   │
│  │              │ └──────┘ │                    │ └───────┘ │ │   │
│  │              │          │                    │           │ │   │
│  │              │ - Docker │                    │ - Docker  │ │   │
│  │              │ - SSH    │                    │ - SSH     │ │   │
│  │              │ - Python │                    │ - Python  │ │   │
│  │              └──────────┘                    └───────────┘ │   │
│  │                                                             │   │
│  │  ┌──────────────────────────────────────────────────────┐ │   │
│  │  │              Persistent Volumes                       │ │   │
│  │  │  - jenkins_home (Jenkins data)                       │ │   │
│  │  │  - fastapi-cache-dev (AI model cache)               │ │   │
│  │  │  - fastapi-cache-prod (AI model cache)              │ │   │
│  │  └──────────────────────────────────────────────────────┘ │   │
│  └───────────────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────────────┘
```

### 🔄 CI/CD Workflow

```
┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
│  User    │      │ Jenkins  │      │ Ansible  │      │  Target  │
│ Triggers │─────▶│ Pipeline │─────▶│ Control  │─────▶│   Node   │
│   Job    │      │          │      │          │      │ (dev/prod)│
└──────────┘      └──────────┘      └──────────┘      └──────────┘
                        │                  │                 │
                        │                  │                 │
                        ▼                  ▼                 ▼
                  1. Build Image    2. Copy Files    3. Deploy App
                  2. Start Container 3. Build Image   4. Run Container
                  3. Execute Ansible 4. Run Playbook  5. Health Check
```

---

## ✨ Features

### 🎯 Core Features
- ✅ **Complete CI/CD Pipeline** with Jenkins
- ✅ **Infrastructure as Code** with Ansible
- ✅ **Multi-Environment Support** (dev/prod)
- ✅ **Containerized Everything** - No local dependencies
- ✅ **SSH Key-Based Authentication** - Secure by default
- ✅ **Persistent Storage** - Data survives container restarts

### 🤖 FastAPI Application
- ✅ **Dual Mode Operation**:
  - **Mock Mode**: Instant responses for development
  - **Full Mode**: Real AI model (distilgpt2) for production
- ✅ **AI Text Generation** using Hugging Face Transformers
- ✅ **Health Check Endpoints**
- ✅ **Environment-Specific Configuration**
- ✅ **Model Caching** - Fast restarts after first run

### 🔧 DevOps Features
- ✅ **Ansible Roles** for modular deployment
- ✅ **Docker-in-Docker** support
- ✅ **Automated Testing** via Jenkins
- ✅ **Volume Persistence** for caches and data
- ✅ **Network Isolation** with Docker networks

---

## 📦 Prerequisites

- **macOS** (tested on macOS 12+)
- **Docker Desktop** (4.0+)
- **Docker Compose** (included with Docker Desktop)
- **4GB RAM** minimum (8GB recommended for Full AI mode)
- **10GB disk space** for images and caches

### Verify Installation

```bash
docker --version
# Docker version 24.0.0 or higher

docker compose version
# Docker Compose version v2.20.0 or higher
```

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
cd ~/Desktop
git clone <your-repo-url>
cd Ansible_Lab/ansible-lab
```

### 2️⃣ Start the Environment

```bash
docker compose up -d --build
```

This will:
- Build all Docker images (~5-10 minutes first time)
- Start all containers
- Create necessary networks and volumes

### 3️⃣ Access Jenkins

1. Open browser: http://localhost:8080
2. Get initial password:
   ```bash
   docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
   ```
3. Install suggested plugins
4. Create admin user (or skip)
5. Save and finish

### 4️⃣ Create Jenkins Pipeline

1. Click **"New Item"**
2. Enter name: `Ansible-Lab`
3. Select **"Pipeline"**
4. Scroll to **Pipeline** section
5. Select **"Pipeline script"**
6. Copy content from `ansible-lab/jenkins/Jenkinsfile`
7. Click **"Save"**

### 5️⃣ Run Your First Deployment

1. Click **"Build with Parameters"**
2. Select environment: `dev` or `prod`
3. Click **"Build"**
4. Watch the pipeline execute!

### 6️⃣ Test the API

```bash
# Health check
curl http://localhost:8001/health

# Make a prediction (mock mode)
curl -X POST http://localhost:8001/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'
```

---

## 📁 Project Structure

```
Ansible_Lab/
├── README.md                          # This file
├── .venv/                            # Python virtual environment
└── ansible-lab/                      # Main project directory
    ├── docker-compose.yml            # Container orchestration
    │
    ├── ansible/                      # Ansible configuration
    │   ├── ansible.cfg              # Ansible settings
    │   ├── inventory/               # Host inventories
    │   │   ├── dev.ini             # Dev environment hosts
    │   │   └── prod.ini            # Prod environment hosts
    │   ├── group_vars/              # Environment variables
    │   │   ├── dev.yml             # Dev configuration
    │   │   └── prod.yml            # Prod configuration
    │   ├── playbooks/               # Ansible playbooks
    │   │   └── deploy_fastapi.yml  # FastAPI deployment
    │   └── roles/                   # Ansible roles
    │       ├── docker/             # Docker installation role
    │       │   └── tasks/
    │       │       └── main.yml
    │       └── fastapi/            # FastAPI deployment role
    │           ├── README.md
    │           └── tasks/
    │               └── main.yml
    │
    ├── control/                      # Ansible control node
    │   ├── Dockerfile               # Control node image
    │   ├── id_ed25519              # SSH private key
    │   ├── id_ed25519.pub          # SSH public key
    │   └── node/
    │       └── authorized_keys     # SSH authorized keys
    │
    ├── node/                         # Managed nodes (dev/prod)
    │   ├── Dockerfile               # Node image
    │   └── authorized_keys         # SSH authorized keys
    │
    ├── jenkins/                      # Jenkins CI/CD
    │   ├── Dockerfile               # Jenkins image
    │   └── Jenkinsfile             # Pipeline definition
    │
    └── fastapi/                      # FastAPI application
        ├── Dockerfile               # App image
        ├── README.md               # App documentation
        ├── requirements.txt        # Python dependencies
        └── app/                    # Application code
            ├── __init__.py
            ├── main.py            # FastAPI app
            ├── model.py           # AI model
            └── schemas.py         # Pydantic models
```

---

## 🔧 Components

### 🎛️ Jenkins (Port 8080)
- **Purpose**: CI/CD orchestration
- **Features**:
  - Pipeline as Code (Jenkinsfile)
  - Multi-environment deployment
  - Docker-in-Docker support
  - Automated testing

### 🤖 Ansible Control Node
- **Purpose**: Configuration management
- **Features**:
  - SSH key-based authentication
  - Modular roles (docker, fastapi)
  - Inventory management
  - Idempotent deployments

### 🖥️ Managed Nodes (dev/prod)
- **DEV Node** (Port 8001):
  - Mock AI mode (fast)
  - Development testing
  - Quick iterations
  
- **PROD Node** (Port 8002):
  - Full AI model (distilgpt2)
  - Production-ready
  - Model caching enabled

### 🚀 FastAPI Application
- **Framework**: FastAPI + Uvicorn
- **AI Model**: distilgpt2 (Hugging Face)
- **Features**:
  - Text generation
  - Health checks
  - Environment awareness
  - Dual mode operation

---

## 📖 Usage

### Managing the Environment

```bash
# Start all containers
docker compose up -d

# Stop all containers (keeps data)
docker compose down

# View logs
docker compose logs -f

# Rebuild after changes
docker compose up -d --build

# Complete cleanup (removes volumes)
docker compose down -v
```

### Accessing Containers

```bash
# Access Ansible control node
docker exec -it ansible-control bash

# Access Jenkins
docker exec -it jenkins bash

# Access dev node
docker exec -it dev bash

# Access prod node
docker exec -it prod bash
```

### Running Ansible Manually

```bash
# Enter control node
docker exec -it ansible-control bash

# Navigate to Ansible directory
cd /ansible/ansible

# Test connectivity
ansible all -i inventory/dev.ini -m ping

# Run playbook manually
ansible-playbook -i inventory/dev.ini playbooks/deploy_fastapi.yml
```

### Switching AI Modes

**Change DEV to Full AI Mode:**
```yaml
# Edit: ansible-lab/ansible/inventory/dev.ini
model_mode=full  # Change from 'mock' to 'full'
```

**Change PROD to Mock Mode:**
```yaml
# Edit: ansible-lab/ansible/inventory/prod.ini
model_mode=mock  # Change from 'full' to 'mock'
```

Then redeploy via Jenkins or manually.

---

## 🌐 API Documentation

### Base URLs
- **DEV**: http://localhost:8001
- **PROD**: http://localhost:8002

### Endpoints

#### Health Check
```bash
GET /health

# Response
{
  "status": "ok",
  "environment": "dev"
}
```

#### Text Prediction
```bash
POST /predict
Content-Type: application/json

{
  "text": "Your input text here"
}

# Response
{
  "result": "Generated text response..."
}
```

### Example Requests

**Mock Mode (Fast):**
```bash
curl -X POST http://localhost:8001/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'

# Response: Instant predefined response
```

**Full Mode (AI):**
```bash
curl -X POST http://localhost:8002/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "The future of AI is"}'

# Response: AI-generated continuation
```

---

## 🐛 Troubleshooting

### Jenkins Can't Access Containers

**Problem**: Jenkins pipeline fails with "container not found"

**Solution**:
```bash
# Ensure all containers are running
docker ps

# Restart Jenkins
docker restart jenkins
```

### Ansible SSH Connection Failed

**Problem**: "Permission denied (publickey)"

**Solution**:
```bash
# Verify SSH keys exist
ls -la ansible-lab/control/id_ed25519*

# Rebuild containers
docker compose down
docker compose up -d --build
```

### FastAPI Container Won't Start

**Problem**: Container exits immediately

**Solution**:
```bash
# Check logs
docker logs dev  # or prod

# Common issues:
# 1. Port already in use
# 2. Missing dependencies
# 3. Syntax error in code

# Rebuild
docker compose up -d --build
```

### AI Model Download Slow

**Problem**: First startup takes forever

**Solution**:
- This is normal for first run (~2 minutes)
- Model is cached in volume for future runs
- Use mock mode for development
- Ensure good internet connection

### Port Already in Use

**Problem**: "port is already allocated"

**Solution**:
```bash
# Find process using port
lsof -i :8080  # or :8001, :8002

# Kill process or change port in docker-compose.yml
```

---

## 🎓 Learning Resources

### Concepts Demonstrated

1. **CI/CD Pipeline**: Jenkins → Ansible → Docker
2. **Infrastructure as Code**: Ansible playbooks and roles
3. **Containerization**: Multi-container Docker application
4. **Configuration Management**: Environment-specific configs
5. **API Development**: RESTful API with FastAPI
6. **AI Integration**: Hugging Face Transformers
7. **DevOps Best Practices**: Automation, testing, deployment


---

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

---

## 🙏 Acknowledgments

- **Ansible** - Configuration management
- **Jenkins** - CI/CD automation
- **FastAPI** - Modern Python web framework
- **Hugging Face** - AI models and transformers
- **Docker** - Containerization platform

---