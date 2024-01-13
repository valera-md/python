# weather.py
# HWl:
# * interactive : while + input() + if/else
# * error messages
# * -> use functions
# HW2: get data["cod"] -> if/else : 404 - not found / 200 - ok

from http.client import HTTPSConnection
from json import loads

key = "api_key_goes_here"
domain = "api.openweathermap.org"
# connect and get data
connection = HTTPSConnection(domain)
def connect(endpoint_current):
 connection.request("GET", endpoint_current)
 response = connection.getresponse()
 return loads(response.read())
# process data
def parse(data):
 return (data['main']['temp'], data['wind']['speed'], data['weather'][0]['description'], data['name'])
def printdata():
 print(f"TEMPERATURE in {location}: {temp}°C")
 print(f"WIND SPEED  in {location}: {wind}m/s")
 print(f"WEATHER     in {location}: {weather}")
#print(f"DATA: {data}", type(data))
#print(f"5tatus: {response.status} and reason: {response.reason}")
while True:
 city = input("Find out the weather in your city. Type in city here or press enter to exit: ")
 if city != "":
  endpoint_current = f"/data/2.5/weather?q={city}&appid={key}&units=metric&lang=ru"
  data = connect(endpoint_current)
  if data["cod"] == 200:
   temp, wind, weather, location = parse(data)
  else:
   input("City was not found, press enter and try another city: ")
   continue
 else:
  connection.close()
  print("Have a nice day.")
  exit()
 printdata()
