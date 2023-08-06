# Day06_HW

### 1. 

list

str

dict

int

complex

float



### 2.

- ```
  __init__ : 인스턴스 생성 시 값을 초기화하는 함수
  ```

- ```
  __del__ : 인스턴스가 소멸될 때 호출되는 함수
  ```

- ```
  __str__ : 특정 객체를 print할 때 보이는 값
  ```

- ```
  __repr__ : 그냥 객체 자체가 호출 될 때 보여주는 값 => print문 없이
  ```



### 3. 

max(): 최대값 반환하기

```
numbers = [5,1,2]
Mx = max(numbers)
print(Mx)   #5
```

min(): 최소값 반환하기

```
numbers = [5,1,2]
mn = min(numbers)
print(mn)   #1
```

count(): 개수 반환하기

```
numbers = [5,1,1,2,1]
cnt = numbers.count(1)
print(cnt)   #3
```

