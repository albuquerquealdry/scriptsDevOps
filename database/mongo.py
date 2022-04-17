import os

PORT = "3000"
IMAGE = "aldry1303"
TAGIMAGE = "despesa"
os.system("cd .. & git clone https://github.com/albuquerquealdry/vagrant-provision.git ")
os.system("cd .. & cd vagrant-provision/dev-environments/mongodb && sed -i 's/IMAGE/'mongo'/g' Vagrantfile")
os.system("cd .. & cd vagrant-provision/dev-environments/mongodb && vagrant up --provision")
#os.system ("cd .. & rm -rf vagrant-provision")