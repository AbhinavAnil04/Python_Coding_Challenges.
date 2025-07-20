import requests
import csv
import time

while True:
  URL=f'http://api.weatherapi.com/v1/current.json?key=267977605d6a448c8e3160901251707&q=kochi'
  r=requests.get(URL)
  data=r.json()
  t=data['current']['temp_c']
  h=data['current']['humidity']
  with open("weather.csv", 'a') as file:
    file.write(f"Temperature: {t}°C, Humidity: {h}%\n")


  time.sleep(3600)

