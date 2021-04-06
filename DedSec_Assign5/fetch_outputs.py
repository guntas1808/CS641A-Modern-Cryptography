import urllib3
import json
from warnings import filterwarnings

filterwarnings('ignore')
http = urllib3.PoolManager(cert_reqs='CERT_NONE') #Creating a Pool Manager

url = "https://172.27.26.181:9997/eaeae"
headers = {'Content-Type': 'application/json'}
fields = {"teamname":"DedSec","password":"45184d2e295477ab95b548089dc6c509","plaintext":"fffffffg"}
data = json.dumps(fields).encode('utf-8')
r = http.request('POST' ,url,  body=data, headers=headers) #http POST request

response = json.loads(r.data.decode('utf-8'))
print(response['ciphertext'])

inputf = open('inputs.txt')
outputf = open('outputs.txt', 'w+')

fields = {"teamname":"DedSec","password":"45184d2e295477ab95b548089dc6c509","plaintext":"fffffffg"}

for line in inputf.readlines(): #read a line from input file
    for word in line.split(' '):
        fields["plaintext"] = word
        data = json.dumps(fields).encode('utf-8')
        r_ = http.request( 'POST', url, body=data, headers=headers)
        resp = json.loads(r_.data.decode('utf-8'))["ciphertext"]
        print(resp)
        outputf.write(resp+" ")
    
    outputf.write("\n")

inputf.close()
outputf.close()