from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')


temperatura = soup.find("img", alt="Temperatura máxima Hoje")
print(temperatura.prettify())
