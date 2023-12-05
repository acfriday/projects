apt-get update

# Install LAMP Server
apt-get install -y lamp-server^

# Docker Engine for Linux installation script from get.docker.com
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh