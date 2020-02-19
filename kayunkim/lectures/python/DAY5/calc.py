def add(num1,num2):
    return num1+ num2

def sub(num1,num2):
    return num1- num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'