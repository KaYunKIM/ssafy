from flask import Flask
from flask import render_template
from flask import request
import requests
import random

from decouple import config

app = Flask(__name__)

token= config('TELEGRAM_BOT_TOKEN')
app_url = f'https://api.telegram.org/bot{token}'
chat_id =  '980615905'

naver_client_id = 't60fBbgqaortkWwIznSB'
naver_client_secret = 'EGnzu8LxNc'

@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    message_url=f'{app_url}/sendMessage?text={text}&chat_id={chat_id}'
    requests.get(message_url)
    return render_template('send.html')

@app.route('/telegram', methods=['POST'])
def telegram():
    import pprint
    response = request.get_json()

    if response.get('message') is not None:
        text = response.get('message').get('text')
        chat_id = response.get('message').get('from').get('id')

        if text[0:4] == '/번역 ':
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]}
            headers = {
                'X-Naver-Client-ID': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            response = requests.post(papago_url, headers=headers, data=data).json()
            text = response.get('message').get('result').get('translatedText')       
        #이 밑에 로또 번호를 보내주는 코드를 작성해주세요!

        if text[0:3] == '/로또':
            numbers = range(1,46)
            lotto= random.sample(numbers, 6)
            text = f'이번 주 행운의 번호는 {lotto}입니다!!!'
          


        
        send_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(send_url)
    
    return '', 200
     


if __name__ == '__main__':
    app.run(debug=True)