import requests
import json 
import os.path
from pprint import pprint as pp


requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"
basedir = os.path.dirname(__file__)

url = "https://api.wallets.africa/bills/airtime/purchase"
url2 = "https://api.wallets.africa/self/verifybvn"

public = "rjhjr8uul9m7"
secret = "st01hemwu0en"

public2 = "uvjqzm5xl6bw"
secret2 = "hfucj5jatq8h"

payload = {#"Code": "etisalat",
           #"Amount": 100,
           #"PhoneNumber": "08097829320",
           "bvn": "22409903043",
           "dateOfBirth": "06-04-1998",
           "SecretKey": secret,
           }
           
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + public,
           }

response = requests.request("POST", url2, headers=headers, data=json.dumps(payload))

#with open(os.path.join(basedir, 'ere.html'), 'w') as file:
#    file.write(response.text)


pp(json.loads(response.text))
