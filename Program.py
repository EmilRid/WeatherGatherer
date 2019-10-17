import requests
from bs4 import BeautifulSoup
import re

weatherURL = "" #weather.com search result 
weatherPage = requests.get(weatherURL) 
weatherSoup = BeautifulSoup(weatherPage.text, "html.parser")

def getTemp(unit): #returns temperature value, unit: celsius or fahrenheit
    farhenheit = int(weatherSoup.find(class_="today_nowcard-temp").get_text()[0:-1])
    if unit == "celsius":
        celsius = round((farhenheit-32)*5/9)
        return celsius
    elif unit == "fahrenheit":
        return farhenheit
    else: 
        print("Check unit for accurate spelling")

def getWeatherType(): #returns Ex. Cloudy, mostly cloudy
    return weatherSoup.find(class_="today_nowcard-phrase").get_text()

def getTable(): #return values with american units coresponding with the RIGHT NOW table on the website
    for obj in weatherSoup.find_all(class_="today_nowcard-sidecar component panel"):
        return str(obj.get_text())

def getWind(unit):#mph or kmh
    print(getTable())
    if unit == "mph":
        return str(getTable()[13:getTable().index("Hum")])
    elif unit == "kmh":
        return getTable()[13:16] + str(round(int(re.sub("\D", "", str(getTable()[13:getTable().index("mph")])))*1.609)) + " km/h" #gets wind speed in kmh