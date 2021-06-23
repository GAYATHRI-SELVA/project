import requests
from datetime import datetime
import urllib.request
import numpy as np

api_key='fa0819d6b1990333dc8d16cf302e9af1'
place=input("Enter The  Name Of The City:")
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_info=api_link.json()
temperature=api_info['main']['temp']
weather=api_info['weather'][0]['desc']
humidity=api_info['main']['humidity']
wind_speed=api_info['wind']['speed']
date_time=datetime.now().strftime(", Date : %d %m %y , Time : %I:%M:%S %p")
print("   * Today Weather Status In  {}  {}".format(place.lower(),date_time))
print("")
print("   * Today Temperature is : {:.2f} deg C ".format(temperature))
print("   * Current Weather Desc :",weather)
print("   * Current Humidity :",humidity,"%")
print("   * Current Wind Speed :",wind_speed,"kmph")
 





