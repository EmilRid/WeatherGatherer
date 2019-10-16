import requests
from bs4 import BeautifulSoup

weatherURL ="https://www.google.com/search?q=weather&rlz=1CAXWWL_enSE816SE816&oq=weather&aqs=chrome..69i57j0l5.851j1j7&sourceid=chrome&ie=UTF-8"
weatherPage = requests.get(weatherURL)
weatherSoup = BeautifulSoup(weatherPage.text, "html.parser")
