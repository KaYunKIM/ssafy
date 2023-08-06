## 2020-10-15 웹소켓 채팅

##### 1. 웹소켓

- 한 번의 request로 서버와 네트워크가 실시간으로 데이터를 주고받을 수 있음

##### 2. 채팅 구현

- 기술스택

  | Vue.js        |
  | ------------- |
  | **Node.js**   |
  | **Socket IO** |

- 서버 구현

  ```javascript
  // 라우팅 및 미들웨어 웹프레임워크 Express 사용
  var app = require('express')(); 
  // http 모듈로 웹서버 만듬
  var server = require('http').createServer(app);
  // 소켓 서버임을 설정
  var io = require('socket.io')(server)
  
  // connection 수립하고 callback인자로 socket을 받는다
  io.on('connection', function(socket){})
  
  // 클라이언트로부터 'chat'이라는 이벤트 명으로 메시지 전달 받는다
  socket.on('chat', function(data){})
  
  // 클라이언트로 'chat'이라는 이벤트 명을 사용해 메시지를 전달한다
  // .broadcast.가 자신을 제외한 나머지 클라이언트에게 메시지를 전달한다
  socket.broadcast.emit('chat', rtnMessage);
  
  ```
  
- 프론트엔드 구현

  ```javascript
  //vue의 main.js
  
  // 서버와 소켓연결을 위한 모듈
  import io from 'socket.io-client';
  
  // 연결하고자 하는 서버의 url 입력
  const socket = io('http://localhost:3001');
  Vue.prototype.$socket = socket;
  ```

  ```javascript
  // 초기 DOM이 생성된 후 한 번 호출되는 created함수에서 socket이벤트를 등록
  // emit을 통해 클라이언트로 메시지를 전달하였으므로, 클라이언트에서 같은 이벤트 명으로 서버로부터 데이터를 받는다
  
  created() { 
      this.$socket.on('chat', (data)=> { 
          this.textarea += data.message + "\n" 
      }) 
  }
  ```

  ```javascript
  // onclick이벤트 발생시, 데이터를 서버로 전송, 현재 입력중인 데이터를 지우기
  sendMessage () { 
      this.$socket.emit('chat',{ message: this.message }); 
      this.textarea += this.message + "\n" 
      this.message = '' 
  }
  ```

  

##### 4.출처

https://javacpro.tistory.com/72