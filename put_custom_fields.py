import requests

# Put Values into Custom Fields from your application for a single person ID

sys = 'Your-System'
sys_key = 'Your-System-Key'
auth = 'Basic YourAuthKey'

person_id = input('Enter Follow Up Boss PersionID: ')
people_url = "https://api.followupboss.com/v1/people/"+str(person_id)

headers = {
  'X-System': sys,
  'X-System-Key': sys_key,
  'Authorization': auth,
  'Content-Type': 'application/json'
}

payload = "{'customLink1' : 'Custom Data1','customLink2' : 'Custom Data2'}"

response = requests.request("PUT", people_url, headers=headers, data = payload)

print(response)
