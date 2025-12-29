FROM quay.io/ansible/ansible-runner:latest

USER root

RUN mkdir -p /root/.ssh
COPY id_ed25519 /root/.ssh/id_ed25519
COPY id_ed25519.pub /root/.ssh/id_ed25519.pub

RUN chmod 600 /root/.ssh/id_ed25519 && \
    chmod 644 /root/.ssh/id_ed25519.pub

WORKDIR /ansible
CMD ["sleep", "infinity"]