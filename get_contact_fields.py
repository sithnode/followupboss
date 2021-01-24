# Get All Follow Up Boss Contact Fields. Both Regular and  Custom fields

import requests as r
import json

sys = 'Your-System'
sys_key = 'Your-System-Key'
auth = 'Basic YourAuthKey'

def get_fub(pid):
	furl = "https://api.followupboss.com/v1/people?id=" + str(pid)
	fields = '&fields=allCustom%2CallFields'
	url = furl + fields
	headers = {
	  'X-System': sys,
	  'X-System-Key': sys_key,
	  'Authorization': auth,
	  'Content-Type': 'application/json'
	}
	results = r.request("GET", url, headers=headers)
	data = results.json()	
	return data['people'][0]
	#return data['people'][0]['customPurchasePrice']

pid = input('Enter Follow Up Boss Person ID: ') #input.get('fub_pid')
data = get_fub(pid)
print(data)
