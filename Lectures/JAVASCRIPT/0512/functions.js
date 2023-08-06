// 선언식 (declaration)
function add(num1, num2) {
    return num1 + num2
}

add(1, 2)

// 표현식 (expression)
/* 아래처럼 이름이 없는 함수를 익명 함수라고 한다.
*/
const sub = function namedSub(num1, num2) {
    return num1  - num2
}

sub(5, 3)
// 기본 인자 (Default Arguments)
const greeting = function(name='nobody'){
    console.log(`${name}`)
}

// Arrow Function
/* 화살표 함수
function에 비해 구문이 짧다. 화살표 함수는 항상 익명이다.
이 함수 표현은 메소드 함수가 아닌 곳에 가장 적합하다.
*/

const arrow = function(name) {
    return `hello ${name}`
}

// AF1. function 키워드 삭제
const arrow = (name) => {return `hello ${name}` }

// AF2. () 생략 (함수 매개변수가 하나일 경우만)
const arrow = name => {return `hello ${name}` }

// AF3. {} & return 생략 (바디가 표현식이 1개일 경우에만)
const arrow = name =>  `hello ${name}`

// AF4. 인자가 없다면? () or _로 표시 가능.
const noArgs = _ => 'No Args'

// AF5. object를 리턴할 때
const returnedObject = () => { return {key: 'value'} }

// AF6. 
const returnedObject = () => ({key: 'value'})

// IIFE (즉시 실행 함수)
/* 선언과 동시에 실행되는 함수
*/ 
(function(num) {
    return num**3
})(2) // 8