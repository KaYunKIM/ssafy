// 0. warmmup - keyword

var a = 10
let b = 10   // 재할당 가능
const c = 10 // 재할당 불가능

// 1. primitive type(원시 타입)
/* primitive type(원시 타입)의 경우 변수에 저장할 때 실제 메모리에 저장된 값을 담게 된다.
*/

// Number
const a = 13
const b = -5
const c = 3.14 // float
const d = 2.99e8 // 2.99*10^8
const e = Infinity
const f = -Infinity
const g = NaN  // Not a Number

console.log(typeof(g))

// String
const sentence1 = 'Ask and go to the blue'
const sentence2 = "Ask and go to the blue"

const firstName = 'Tony'
const lastName = 'Stark'
const fullName = firstName + lastName
console.log(fullName)

const word = "안녕 \n하세요"    //줄바꿈

// String - Template Literal
/* ES6+부터 지원한다.
Backtic(`)를 이용하며, 여러 줄에 걸쳐 문자를 정의 할 수도 있고
JS의 변수를 문자열 안에 바로 연결할 수 있는 이점이 생긴다.
*/

const ssafy = '5반'
const word2 = `${ssafy} 안녕들
하세요`

//Boolean
true
false

// Empty Value (null, undefined)
/* 값이 존재하지 않음을 표현하는 값으로 null과 undefined가 있다.
동일한 역할을 하는 두 개의 키워드가 존재하는 이유는 단순한 설계 
*/

let firstName
console.log(firstName)  // undefined

let lastName = null
console.log(lastName)  // null


// 2. 연산자
// 할당연산자
let number = 0

number += 10
console.log(number)

number -= 10

number *= 10

number++  // number에 1일 더하다(증감식)

number--  // number에 1일 뺀다(증감식)

//비교연산자
3 > 2 // true
3 < 2 // false

'A' < 'B' // true
'z' < 'a' // false
'a'.codePointAt(0)
'z'.codePointAt(0)

// 동등연산자(==)
/* 메모리의 같은 객체를 가리키거나 같은 값을 갖도록 형(type)을 변환할 수 있다면 서로 같다고 판단.*/

const a = 1
const b = '1'

console.log(8*null) //0
console.log('5' - 1) //4
console.log('5' + 1)// 51
console.log('five' * 2) // Nan

// 일치연산자(==)
const a = 1
const b = '1'

// 논리연산자
true && true // true
true && false // false

1 && 0 // 0
0 && 1 // 0
4 && 7 // 7

false || true // true
false || false // false

1 || 0 //1
0 || 1 // 1
4 || 7 // 4

// not 연산자
!true  // false

// 삼항 연산자(Ternary Operator)
true ? 1 : 2 // 1
false? 1 : 2 // 2

const result = Math.PI > 4 ? 'Yep' : 'Nope'
console.log(result)

let age = 21
let message = age < 7 ? '애기입니다' : 
    age < 30 ? '청소년입니다' :
    age < 100 ? '어른입니다' :
    '사람입니다'