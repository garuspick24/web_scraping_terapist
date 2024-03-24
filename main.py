import requests
from bs4 import BeautifulSoup

url = 'https://www.psychologytoday.com/us/therapists/ny/brooklyn'
responce =  requests.get(url)
html = responce.text

soup = BeautifulSoup(html, 'html.parser')
