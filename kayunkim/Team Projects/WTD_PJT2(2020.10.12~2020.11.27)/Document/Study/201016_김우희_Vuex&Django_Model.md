### Vuex 시작하기

1. Vuex 란?

   - Vue.js의 **상태 관리**를 위한 패턴이자 라이브러리	

     

2. 상태 관리

   - 여러 컴포넌트 간의 데이터 전달과 이벤트 통신을 한곳에서 관리하는 패턴을 의미

   - **컴포넌트 간의 통신이나 데이터 전달을 좀 더 유기적으로 관리** 하기 위해

     

3.  상태 관리 패턴

   - **state** : 컴포넌트 간에 공유할 **data**
   - **view** : 데이터가 표현될 **template**
   - **actions** : 사용자의 입력에 따라 반응할 **methods**
   - **mutations** : state 값을 변경하기 위한 



### Django Model

- N : M (ex 팔로워, 팔로잉)

  [ User로 다대다를 이루고 있기 때문에 self로 선언 ]

  follwers = models.ManyToManyField("self")

  follwing = models.ManyToManyField("self")

  

- 외래키 사용시

   models.Foreignkey(

  ​                  user_model.User, 

  ​                  null=ture, 

  ​                  on_delete=models.CASCADE,  -> 외래키로 사용되고 있는 user가 

  ​                                                                            삭제되면 어떻게 처리가 될 것인가

  ​                  related_name='post author' 

    )