2020-10-15(木)





## Vuex 간단하게



### Vuex..

* React의 Flux 패턴에서 기인했다고 함.

  (참고) Flux 패턴이란..

  MVC 패턴의 복잡한 데이터 흐름 문제를 해결하는 개발 패턴 - Undirectional data flow

  - 아래의 순서로 **단일 방향**으로만 흐름이 흘러간다.
    1. actions : 화면에서 발생하는 이벤트 또는 사용자의 입력
    2. dispatcher : 데이터를 변경하는 방법, 메서드(model을 바꾸기 위한 역할)
    3. model : 화면에 표시할 데이터
    4. view : 사용자에게 비춰지는 화면, 화면에서 다시 action을 호출하게 된다. 그러면 다시 1->2->3->4 한 방향 흐름.



복잡한 애플리케이션에서 컴포넌트의 개수가 많아지면 컴포넌트 간에 데이터 전달이 어려워진다.

- 로그인 폼에서 id를 하위 컴포넌트로 계속해서 전달해서 내려야 할 때, 중간에 거치는 컴포넌트들이 많아 질수록 계속해서 props를 선언해야 하므로 데이터 전달이 불편해진다.

  -- 그래서 Vuex가 필요하다고 한다~!



#### 그래서 전체 구조는??

**State** : 컴포넌트 간에 공유하는 데이터 `data()`

**View** : 데이터를 표시하는 화면 `template`

**Action** : 사용자의 입력에 따라 데이터를 변경하는 `methods`

**단방향 데이터 흐름** 처리를 단순하게 도식화한 그림

- View(Template)에서 버튼을 클릭했을때, 클릭이라는 Action(Method)이 발생한다.
- 해당 Action이 동작을 통해서 State(data)를 변경한다.

알던 거랑 이름만 다른 정도.



#### 특별한 내용은 없는 듯 하다.



## Django M:N

#### 1:N일때는?

N쪽의 레코드가 1쪽의 레코드에 속함

#### M:N일 경우는?

1:N의 테이블을 2개 생성해서, 2개의 테이블의 PK를 데이터로 갖는 테이블을 생성함.

**1:N 2개 생성으로 만드는 듯 하다.**



#### 근데 테이블 생성 없이도 M:N을 direct로 만들 수 있다.

바로 

```python
ManyToManyField("연결할 모델 클래스 이름")
```

의 형태로 ...?

**사용 예시**

```python
class Client(models.Model):
    name = models.CharField(max_length=30)
    
    
class Resort(models.Model):
    name = models.CharField(max_length=30)
    clients = models.ManyToManyField(Client)
```



생각보다 간단한듯.

