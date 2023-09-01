import requests

initiate_url = 'http://localhost:10210/movements'
myobj = {'somekey': 'somevalue'}

x = requests.post(initiate_url)

print(x.text)