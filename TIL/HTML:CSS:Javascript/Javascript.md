

JavaScript 기초

### 데이터 타입 분류(typeof)







- 원시 타입(primitive)- 변경 불가능한 값(immutable)

  - Boolean: T/F
  - null
  - undefined
  - number: 모든 숫자는 number 타입
  - string
  - symbol(ES6)  

- 객체타입(object)

  - Object: 일반 객체, function, array, date, RegExp

  

자바스크립트는 원시 타입을 제외하고는 모두 객체이다.

자바스크립트의 객체는 키 외 값으로 구성된 속성의 집합이며, 프로퍼티 값이 함수일 경우 구분을 위해 메소드라고 부른다.



자바스크립트는 함수 레벨 스코프를 가진다.

따라서 함수 내에서 선언된 변수는 지역(local)변수이며, 나머지는 전역(global) 변수로 활용된다.

#### 변수 선언 시 키워드(var) 쓰지 않으면, 암묵적 전역으로 설정된다



####  자바스크립트는 모든 선언(var)을 호이스팅 한다.  => let/const로 방지

#### ES6에서 새롭게 등장한 let과 const키워드는 이러한 내용 방지할 수 있다.



연산자: 일치연산자(===)

동등연산자: (==)

조건문: else if

<hr>

객체는 Key와 value로 구성된 속성들의 모임

객체는 암묵적 형변환 일어난다 => 그게 아닐 경우, ""를 사용해 문자열로 만들어 주어야 한다

For in 은 객체의 모든 값 순회

#### 배열(Array)메소드

sort 함수에 비교인자 없으면 문자열 기준 정렬 : 1,100,2,3,4

```
var numbers = [4,2,5,1,3,100]:
numbers.sort(function(a,b)){
	return a-b;
})
```

- 문자열 관련 - join, toString

- 배열합치기 - concat(문자열로 바꿔서 합친다)

```
var a= [1,2,3]
a.concat([4,5])
=> [1,2,3,4,5]
a+[4,5]
=> "1,2,34,5"
a.concat(4,5)
[1,2,3,4,5]
```

- 원소 삽입/삭제 : push,pop,unshift(가장 처음 인덱스 push),shift(가장 처음 인덱스 pop)
- 인덱스 탐색: indexOf(string과 Array 둘다 사용 가능) - 없으면 -1반환, 있으면 문자열의 첫번째 인덱스 반환
- 배열조작: splice(원본 배열 자체 바꿈, 원본 수정/삭제 가능)/ slice(새로운 값으로 그냥 리턴)
- 자바스크립트 join: 배열문법/ 파이썬 join: 문자열 문법
- 배열(Array)순회: for/for..of/forEach.  #for..in(배열 지정 property까지 모두 다 출력)





## DOM(Document Object Model)

문서의 구조화된 표현 제공, DOM구조에 접근할 수 있는 방법 제공

문서의 구조/스타일/내용 등 변경을 도우며, 구조화된 노드와 object로 문서 표현

- 주요객체
  - Window: DOM문서 표현하는 창(가장 최상위 객체) - 다양한 함수, 이름공간, 객체 등 포함
  - Document: <body>등 다른 요소 포함
  - navigator, location. History, screen

- DOM 접근
  - 단일 Node- document.querySelector(selector)
  - NodeList(non-live) - document.querySelectorAll(selector)



## EVENT

이벤트 전파

- Event는 해당 요소에서 전파되며, 캡처링과 버블링으로 구분된다.



## JavaScript Advanced Function

### 함수 호이스팅

자바스크립트에서 모든 선언은 호이스팅

- 함수 선언문: 선언, 초기화, 할당 모두 이루어져 실행 가능
- 함수 표현식은 변수 호이스팅이 발생하여 undefined, 즉 실행 불가=> 주로 위주로 작성함



## JavaScriot Closure

### First class function

자바스크립트 함수는 아래와 같은 특징 지님

- 함수를 인자로 전달 가능
- 함수를 반환 가능
- 변수에 함수 할당 가능

  위  조건은 프로그래밍 언어에서의 일급 객체(first class object)의 조건이다.



