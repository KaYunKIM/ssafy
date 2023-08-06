2020-10-15(木)





## 장고 DB 기초 공부

참고 : https://velog.io/@magnoliarfsit/ReDjango-3.-GET-POST-%EB%A9%94%EC%86%8C%EB%93%9C-%EC%B0%A8%EC%9D%B4%EC%A0%90-%EB%B0%8F-api-%EC%84%A4%EA%B3%84

### GET

백엔드에서 쿼리스트링 받을 때 : 장고에서는 **query parameter의 key와 value는 request의 GET 객체로 쿼리 딕셔너리로 담겨서 들어온다.**

ex) sort_by = request.GET.get('sort_by', None)  **-- 없으면 None, key 값에 해당하는 게 있으면 value 인 듯.**



**requeset.GET vs request.GET.get() **	-- 알아두면 좋을듯

request.GET은 GET으로 받는 파라미터들을 다 포함하는 딕셔너리 객체이다.
get() 메서드는 key 값이 딕셔너리 안에있으면 value값을 리턴해준다. 키 값이 존재하지 않으면 디폴트값인 None을 리턴한다.
request.GET.get()은 위 두 개념을 합친것으로 GET 요청이 접근할 수 있는 key와 value 값을 이용한다.



### POST

#### json 방식 

```python
data = json.loads(request.body)
```

```python
data = json.loads(request.body)
            if len(data.keys()) < 6:
                return HttpResponse(status=400)
            for value in data.values():
                if value in "":
                    return HttpResponse(status=400)
```



#### Data 반환 방식

```null
area_info = [
                {
                    "area_name" : area.name,
                    "area_code" : area.code,
                    "clickable" : area.branch_set.exists()
                } for area in region.area_set.all()
            ]
            return JsonResponse({"area_info": area_info}, status=200)
```



## ORM

#### <u>Create?</u>

#### 방법1. 각 Model Instance의 save 함수를 통해 저장

```python
model_instance = Post(author=User.objects.all()[0], title='title', text='content')
model_instance.save()  
```

#### 방법2. 각 Model Instance의 create 함수를 통해 저장

```python
new_post = Post.objects.create(author=User.objects.get(id=1), title='title', text='content')
```

- .save() 와 .create() 실행시 DB에 INSERT SQL이 전달된다.
- <u>중요한건 필드 지정 꼭 해야하는 것 같다...?</u>



#### <u>Retrieve?</u>

```python
queryset = 모델클래스명.objects.all()
queryset = queryset.filter(조건필드1=조건값1, 조건필드2=조건값2)
queryset = queryset.filter(조건필드3=조건값3)
```

* 조건주고 조회하면 된다.

```python
모델클래스명.objects.all().filter(Q(조건필드1=조건값1) | Q(조건필드2=조건값2)) # or 조건
모델클래스명.objects.all().filter(Q(조건필드1=조건값1) & Q(조건필드2=조건값2)) # and 조건
```

* 이런식으로 or과 and 조건을 구별할 수도 있음.



#### 특정필드 기준 정렬조건 (Meta.ordering)

- queryset의 기본 정렬은 모델 클래스 내부의 [Meta.ordering](https://docs.djangoproject.com/en/3.0/ref/models/options/#ordering) 설정을 따른다.

```python
# myapp/models.py
#
class Post(models.Model):
  ....
  class Meta:
    ordering = ['-id'] # id 필드 기준 내림차순 정렬, 미지정시 임의 정렬
```

- 모델 Meta.ordering 을 무시하고 직접 정렬조건 지정도 가능하다. -- 이것만 알아도 괜찮을듯

```python
ordering = ['pub_date'] # 지정 필드 오름차순 요청
ordering = ['-pub_date'] # 지정 필드 내림차순 요청
ordering = ['-pub_date', 'author'] # 1차기준, 2차기준
```



#### <u>Update?</u>

#### 방법1. 각 Model Instance 속성을 변경하고, save 함수를 통해 저장

- 각 Model 인스턴스 별로 SQL 수행
- 다수의 Row에 대해서 수행 시 성능저하

```python
post_instance = Post.objects.get(id=66)
post_instance.title = 'edit title' # title 수정
post_instance.save()

queryset = Post.objects.all()
for post in queryset:
    post.tags = 'Python, Django'
    post.save() # 각 Model Instance 별로 DB에 update 요청 - 성능저하
```

#### 방법2. QuerySet의 update 함수에 업데이트할 속성값을 지정하여 일괄 수정

- 하나의 SQL 로서 동작하므로 동작이 빠르다. -- 전체 수정하기 편할듯

```python
queryset = Post.objects.all()
queryset.update(title='test title') # 일괄 update 요청
```



#### Delete?

#### 방법1. 각 Model Instance의 delete 함수를 호출하여 삭제

- 각 Model 인스턴스 별로 SQL 수행
- 다수의 Row에 대해서 수행 시 성능저하

```python
post_instance = Post.objects.get(id=66)
post_instance.delete()

queryset = Post.objects.all()
    for post in queryset:
    post.delete() # 각 Model Instance 별로 DB에 delete 요청 - 성능저하
```

#### 방법2. QuerySet의 delete 함수를 호출하여, 관련 데이터 삭제

- 하나의 SQL 로서 동작하므로 동작이 빠르다.

```python
queryset = Post.objects.all()
queryset.delete() # 일괄 delete 요청
```



### <u>기타 질문해서 알아낸 내용</u>

* Serializer 같은 경우, 모델이 1:N과 같이 여러개 일 경우 따로 mapping 해주는 개념으로 보임.
* fileds ='_all_' 해서 모든 filed가 다 들어가는 내용

