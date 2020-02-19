import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://www.daum.net'

response = requests.get(url)
response = response.text
data = BeautifulSoup(response, 'html.parser')

result = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol> li> div> div')
print(result)