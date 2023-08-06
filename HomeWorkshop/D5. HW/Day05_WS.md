# Day05_WS

### 1. 

``` 
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
```



### 2.

```
from calc import add
from calc import sub
from calc import mul
from calc import div

num1, num2 = map(int, input().split())
print(add(num1, num2))
print(sub(num1, num2))
print(mul(num1, num2))
print(div(num1, num2))
```

```
import calc

num1, num2 = map(int, input().split())
print(calc.add(num1, num2))
print(calc.sub(num1, num2))
print(calc.mul(num1, num2))
print(calc.div(num1, num2))
```