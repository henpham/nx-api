"""
 NX-API-BOT 
"""
import requests
import json

"""
Modify these please
"""
url='http://172.16.1.136/ins'
switchuser='admin'
switchpassword='admin'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

print "Hello!"

##print response

print response['jsonrpc']
result = response['result']
body = result['body']
print ('The kick start version is ' + body['kickstart_ver_str'] + ' and the host name is ' + body['host_name'])