# search.py
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

response = requests.get(url).text
data=BeautifulSoup(response, 'html.parser')

search = data.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
print(search)
for i in search: 
    print(i.text)
