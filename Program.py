import requests
from bs4 import BeautifulSoup

unit = "celsius" #unit of measurement 
weatherURL = "https://weather.com/weather/today/l/8b2acedf23be2811693b172400157817be1e2c7b9962e5db45ee1a5f94a59a9c" #weather.com search result 
weatherPage = requests.get(weatherURL) 
weatherSoup = BeautifulSoup(weatherPage.text, "html.parser")

def getTemp(): #returns temperature value
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

