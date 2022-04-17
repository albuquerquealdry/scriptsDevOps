import os
import time
import requests
import dotenv


os.system("cd .. & git clone https://github.com/albuquerquealdry/vagrant-provision.git ")
os.system(f"cd .. & cd vagrant-provision/dev-environments/aplication-node/nodeAplication && sed -i 's/IMAGE/'{IMAGE}'/g' Vagrantfile && sed -i 's/PORT/'{PORT}'/g' Vagrantfile && sed -i 's/PROVIDER/'{PROVIDER}'/g' Vagrantfile && sed -i 's/TAGVERSION/'{TAGVERSION}'/g' Vagrantfile && sed -i 's/TAGAPLICATION/'{TAGAPLICATION}'/g' Vagrantfile " )
os.system("cd .. & cd vagrant-provision/dev-environments/aplication-node/nodeAplication  && vagrant up --provision")

time.sleep(3)
url = f"{METHOD}{HOST}:{PORT}/{ENDPOINT}"
request = requests.get(url).status_code
if request == 200 or 201:
    n = 0
    print ("TESTING APLICATION")
    while n != 10:
        n = n+1
        request = requests.get(url).status_code
        print(request)
    os.system ("cd .. & cd vagrant-provision/dev-environments/aplication-node/nodeAplication && vagrant destroy -f ")
    os.system ("cd .. & rm -rf vagrant-provision")
    
else:
    print ("Application NO OK")
    os.system ("cd .. & cd vagrant-provision/dev-environments/aplication-node/nodeAplication && vagrant destroy -f ")
    os.system ("cd .. & rm -rf vagrant-provision")
