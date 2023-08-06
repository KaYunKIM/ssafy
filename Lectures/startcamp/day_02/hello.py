from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup

from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ssafy')
def ssafy():
    return '짜잔!'

@app.route('/dday')
def dday():
    today = datetime.now()
    endgame = datetime(2020, 5, 29)
    td = endgame - today
    return f'{td.days}일 남았습니다!'

@app.route('/html')
def html():
    return '<h1>안녕하세요!!!</h1>'

@app.route('/html_lines')
def html_lines():
    return """
    <h1>여러줄을 보내봅시다!</h1>
    <ul>
       <li>1번</li>
       <li>2번</li>
    <ul>
    """

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!' 

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다!!'

@app.route('/lunch/<int:people>')
def lunch(people):
    import random
    menu = ['김밥', '라면', '돈까스', '짜장']
    order = random.sample(menu,k=people)
    return  str(order)

@app.route('/ssafy5')
def ssafy5():
    return render_template('ssafy5.html')

@app.route('/greeting2/<string:name>')
def greeting2(name):
    return render_template('greeting2.html', html_name=name)

@app.route('/cube2/<int:number>')
def cube2(number):
    result = number**3
    return render_template('cube2.html', number=number, result=result)

@app.route('/movie')
def movie():
    movies = ['겨울왕국', '포드앤페라리', '스파이더맨']
    return render_template('movie.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
     name = request.args.get("name")
     return render_template('pong.html', name_in_html=name)


@app.route('/naver')
def naver ():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')


@app.route('/godmademe')
def godmademe():
     name = request.args.get("name")
     first_list = ['미모', '기럭지', '브레인', '인성']
     second_list = ['자신감', '허세', '애교', '잘난척']
     third_list = ['돈', '식욕', '물욕']


     first = random.choice(first_list)
     second = random.choice(second_list)
     third = random.choice(third_list)
     return render_template('godmademe.html', name=name, first=first, second=second, third=third)



@app.route('/bday')
def is_bday():
    today = datetime.now()
    if today.month == 1 and today.day == 16:
        result = True
    else:
        result = False
    return render_template('bday.html', result=result)


@app.route('/dust')
def dust():
    

    api_key = '18sdqPnoqMEjN5FERbhv5tqJ%2BJzN7VX%2FMWseSnqgnxjcMc6rqTp%2FJZnI%2ByGiQo5ep9WI6%2F9oVMoqrMhvlHyCdA%3D%3D'
    url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={api_key}&numOfRows=40&pageNo=1&startPage=3&sidoName=서울&ver=1.6'

    response = requests.get(url).text
    data = BeautifulSoup(response, 'html.parser')

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

    
    today = datetime.now()
    return render_template('dust.html', dust_rate = dust_rate, today=today)





if __name__== '__main__':
    app.run(debug=True)
