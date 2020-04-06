import requests
from pprint import pprint

city = input("Please enter the city: ")

# requesting the data via api call
url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=7eb40057865a9784096c8925009a7ce4&units=metric')

# fetching data in json format
data = url.json()
# pprint is used to show the data in a more human readable format
pprint(data)

# iterating over items in data
# for i in data.items():
# 	print(i)

# fetching the temperature

temperature	= data['main']['temp']
# fetching the city name
name = data['name']
image = data['weather'][0]['icon']
print(f'Temperature of {name} is {temperature}')
print(image)