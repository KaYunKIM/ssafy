// Function Scope - var를 사용할 때

function number(num) {
    var acc = num + 1
    return acc
}

console.log(acc)

if (true) {
    var name = '용우와 영수'
}

console.log(name)

// Block Scope - const, let을 사용할 때
if (true) {
    let age = '100'
}

console.log(age)

function numberTwo(num) {
    let accTwo = num + 1
    return accTwo
}

console.log(accTwo)