import requests
import json

# Get Custom Fields from you application

sys = 'Your-System'
sys_key = 'Your-System-Key'
auth = 'Basic YourAuthKey'
customfields_url = "https://api.followupboss.com/v1/customFields?limit=1000"

payload = {}
headers = {
  'X-System': sys,
  'X-System-Key': sys_key,
  'Authorization': auth
}
r = requests.request("GET", customfields_url, headers=headers, data = payload)
r = r.json()

custom = {}

i = 0
while i < len(r['customfields']):
    custom[r['customfields'][i]['name']]='value'
    i = i+1
print(custom)
