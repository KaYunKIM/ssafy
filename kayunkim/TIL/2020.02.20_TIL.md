2020.02.20(Thu)

# OOP

Object Oriented Programming : 객체 지향 프로그래밍



python의 모든 것은 객체이다.



### User with OOP

서비스를 만들었다고 가정하고, 사용자들이 로그인을 한 뒤 해당 정보를 기록할 클래스를 만들어봅시다.

*self

전세계 모든 사용자가  self 쓴다!



instance의 속성은 공유되지 x





```
def my_sqrt():
    x, y = 1, n
    result = 1

    while abs(result**2 -n) > 0.00000001:
        result = (x+y) /2
        if result **2 < n:
            x = result
        else:
            y = result
    return result

print('my_sqrt:\t',my_sqrt(2))

import math
print('math.sqrt:\t',math.sqrt(2))
```