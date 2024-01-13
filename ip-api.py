#ip-api.py
name = input("enter domian name or ip address: ") # "mail.ru"
address = f"http://ip-api.com/json/{name}"

import requests
response = requests.get(address)
data = response.json()
#print(type(data))
#print(data)
#HM1: check if succes
if data["status"] == "success":
 print("region", data["regionName"])
 print("organization", data["org"])
else:
 print("no information found")
