import requests
from bs4 import BeautifulSoup

unit = "" #unit of measurement 
weatherURL = "" #weather.com search result 
weatherPage = requests.get(weatherURL) 
weatherSoup = BeautifulSoup(weatherPage.text, "html.parser")
farhenheit = int(weatherSoup.find(class_="today_nowcard-temp").get_text()[0:-1])

if unit == "celsius":
    celsius = (farhenheit-32)*5/9
    print(round(celsius),"C")

elif unit == "fahrenheit":
    print(farhenheit, "F")

else: 
    print("Check unit for accurate spelling")