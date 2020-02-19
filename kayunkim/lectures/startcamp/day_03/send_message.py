import requests
import pprint

#1. 기본 설정
token = '1030095326:AAGSfDW20dpOkapcx-6OwSL3wVchxCuXgb4'
app_url = f'https://api.telegram.org/bot{token}'

#2. getUpdates 요청하기
update_url = f'{app_url}/getUpdates'
response = requests.get(update_url).json()

data = response['result'][0]['message']['chat']['id']
text = 'Thank God, it is Friday! TGIF!!'

#3. 텔레그램으로 메세지 보내기
message_url = f'{app_url}/sendMessage?text={text}&chat_id={data}'
requests.get(message_url)