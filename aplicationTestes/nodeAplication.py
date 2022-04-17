import os
import time
import requests

HOST = "localhost"
METHOD = "http://"
ENDPOINT = "receita"

PORT = "3000"
IMAGE = "despesa"
TAGAPLICATION = "despesa"
PROVIDER = "aldry1303"
TAGVERSION = "1.0.2"

os.system("cd .. & git clone https://github.com/albuquerquealdry/vagrant-provision.git ")
os.system(f"cd .. & cd vagrant-provision/dev-environments/aplication-node/nodeAplication && sed -i 's/IMAGE/'{IMAGE}'/g' Vagrantfile && sed -i 's/PORT/'{PORT}'/g' Vagrantfile && sed -i 's/PROVIDER/'{PROVIDER}'/g' Vagrantfile && sed -i 's/TAGVERSION/'{TAGVERSION}'/g' Vagrantfile && sed -i 's/TAGAPLICATION/'{TAGAPLICATION}'/g' Vagrantfile " )
os.system("cd .. & cd vagrant-provision/dev-environments/aplication-node/nodeAplication  && vagrant up --provision")
os.system ("cd .. & rm -rf vagrant-provision")

url = f"{METHOD}{HOST}:{PORT}/{ENDPOINT}"
teste = requests.get(url).status_code
print(teste)
if teste == 200 or 201:
    print ("TESTING APLICATION")
    time.sleep(120)
    os.system ("cd .. & cd vagrant-provision/dev-environments/aplication-node/nodeAplication && vagrant destroy -f ")
    
else:
    print ("Application NO OK")
