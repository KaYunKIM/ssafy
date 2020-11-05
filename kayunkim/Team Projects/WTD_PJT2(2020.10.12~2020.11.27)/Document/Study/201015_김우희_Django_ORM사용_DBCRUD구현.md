## Django [ DB CURD ]

##### 장고 ORM을 사용해서 DB CRUD 구현하기



- Create

```python
model_instance = Post(author=User.objects.all()[0], title='title', text='content')
model_instance.save()  
```



- Retrieve 

>  AND

```python
queryset = 모델클래스명.objects.all()
queryset = queryset.filter(조건필드1=조건값1, 조건필드2=조건값2)
queryset = queryset.filter(조건필드3=조건값3)
```

>  OR

```python
모델클래스명.objects.all().filter(Q(조건필드1=조건값1) | Q(조건필드2=조건값2)) # or 조건
모델클래스명.objects.all().filter(Q(조건필드1=조건값1) & Q(조건필드2=조건값2)) # and 조건
```



- Update

```python
post_instance = Post.objects.get(id=66)
post_instance.title = 'edit title' # title 수정
post_instance.save()
```



- Delete

```python
post_instance = Post.objects.get(id=66)
post_instance.delete()
```





참조 블로그
[초보몽키의 개발공부로그](https://wayhome25.github.io/django/2017/04/01/django-ep9-crud/)
[7. 모델을 통한 데이터 CRUD](https://jjinisystem.tistory.com/31)