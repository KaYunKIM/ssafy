import requests
from bs4 import BeautifulSoup

api_key = '18sdqPnoqMEjN5FERbhv5tqJ%2BJzN7VX%2FMWseSnqgnxjcMc6rqTp%2FJZnI%2ByGiQo5ep9WI6%2F9oVMoqrMhvlHyCdA%3D%3D'
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={api_key}&numOfRows=40&pageNo=1&startPage=3&sidoName=서울&ver=1.6'

response = requests.get(url).text
data = BeautufulSoup(response, 'html.parser')

items = data.find_all('item')
location = items[27]

gangnam_dust = location.pm10value.text
gangnam_dust = int(gangnam_dust)


if gangnam_dust > 150:
    dust_rate='매우 나쁨'
elif 80< gangnam_dust <= 150:
    dust_rate = '나쁨'
elif 30 < gangnam_dust and gangnam_dust <=80:
    dust_rate = '보통'
else:
    dust_rate = '매우 좋음'

print(dust_rate)