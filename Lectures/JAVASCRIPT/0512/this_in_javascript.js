// 0.
console.log(this)

// 1. "this" with function
const data = {
    url: 'https://www.naver.com', 
    showUrl: function() {return this}, 
}

console.log(data.showUrl()) // data 객체
// 2. "this" with arrow function
const dataTwo = {
    url: 'https://www.naver.com',
    showUrl: () => {return this}
}