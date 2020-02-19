# kospi.py
import requests
from bs4 import BeautifulSoup

response = requests.get('http://finance.naver.com/sise/').text
data=BeautifulSoup(response, 'html.parser')
kospit = data.select_one('#KOSPI_now')
print(kospi.text)

