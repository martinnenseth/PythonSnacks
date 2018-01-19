import requests
import re
from bs4 import BeautifulSoup

page = requests.get(("https://coinmarketcap.com/"))
page = page.text
soup = BeautifulSoup(page, "html.parser")
soup.prettify()
litecoin = soup.find(id='id-litecoin')

price = litecoin.find_all('a', href="/currencies/litecoin/#markets")
print(price[0].string)