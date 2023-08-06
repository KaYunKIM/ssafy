# Day07_HW

### 1. 

Instance method: info(self)		

Staticmethod: add(a,b)

Classmethod: history(cls)



### 2.

```
cal1 = Calculator()
```

```
cal.info()   #나는 계산기입니다.
```

```
cal.add(4,5)  #4+5는 9입니다.
```

```
cal.history()  #총 1번 계산했습니다.
```



### 3.

파라미터 self와 cls에는 어떤 값이 할당 되는지 작성하시오.

- 인스턴스 메서드 생성 후 자동으로 인스턴스 객체가 self가 된다.
- 클래스 메서드에서 첫 번째 인자로  cls를 받을 때, 자동으로 클래스 객체가 cls가 된다.

