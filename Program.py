import requests
from bs4 import BeautifulSoup

weatherURL = "https://weather.com/weather/today/l/8b2acedf23be2811693b172400157817be1e2c7b9962e5db45ee1a5f94a59a9c" #weather.com search result 
weatherPage = requests.get(weatherURL)
weatherSoup = BeautifulSoup(weatherPage.text, "html.parser")

print(weatherSoup.find(class_="today_nowcard-temp").get_text())
