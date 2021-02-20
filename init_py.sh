# UTC to KST
sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# python3 -> python
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# pip3 -> pip
sudo apt-get update
sudo apt-get install -y python3-pip
pip3 --version
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1