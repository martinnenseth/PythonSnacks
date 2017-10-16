import requests as rq
from bs4 import BeautifulSoup as bs

url = "http://www.uia.no"
r = rq.get(url)
data = r.text
soup = bs(data, "html.parser")

for link in soup.find_all('a'):
    innerurl = link.get('href')
    s = rq.get(innerurl)
    innerdata = s.text
    innersoup = bs(innerdata, "html.parser")
