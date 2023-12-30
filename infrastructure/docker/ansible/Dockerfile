FROM ubuntu:20.04
RUN apt-get -y update && apt-get -y install \
	ansible \
	vim \
	openssh-client

COPY inventory.ini .
COPY ansible.cfg .
RUN ssh-keygen -t ed25519 -N "" -C "ansible" -f ~/.ssh/ansible