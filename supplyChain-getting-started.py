import json
import requests
from requests.auth import HTTPBasicAuth

url = 'http://192.168.2.8:7755/'
headers = {'content-type': 'application/json'}

payload = {"method":"getinfo","params":[],"id":1,"chain_name":"supplyChain"}

r = requests.post(url, data=json.dumps(payload), headers=headers, auth=HTTPBasicAuth('multichainrpc', 'HQYxx31kGsdUsV5Q2THPkpbzUyBaNe5i2Xv6ZW7MiMLe'))

print(r.text)
