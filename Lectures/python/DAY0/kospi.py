import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/sise/').text
data = BeautifulSoup(response, 'html.parser')
kospi = data.select_one('#KOSPI_now')
print(kospi.text)