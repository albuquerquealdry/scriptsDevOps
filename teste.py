import os
import requests

url = "http://localhost:3000/receita"
teste = requests.get(url).status_code
print (teste)
if teste == 200:
    print ("Application OK")
else:
    print ("Application n OK")
