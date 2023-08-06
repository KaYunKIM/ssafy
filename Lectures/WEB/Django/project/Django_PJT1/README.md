# Django_pjt1

1. 프로젝트 구조
django_pjt1, community, templates를 같은 경로에 위치하게 만들었습니다.


2. Model
models.py에서Review 클래스를 정의한 뒤 title은 CharField로 길이를 주고, content는 길이 제한 없는 TextField로, rank는 IntegerField로 변수 생성을 했습니다.
리뷰 작성시간과 수정 시간은 DateTimeField를 주어 자동 저장 기능을 추가했습니다.



3. Admin
admin.py에서 위에 만들어 두었던 models 내 Review 클래스를 불러와 admin.site.register에게 상속해 관리자 페이지를 관리할 수 있습니다.
이후 python manage.py createsuperuser로 관리자 페이지에 로그인 할 아이디와 비밀번호를 생성했습니다.

4. URL
community/urls.py와 django_pjt1/urls.py 2개의 url로 나누어

community/urls.py에는 django_pjt1/urls.py에서 넘어오는 url을 받아 뒤에 추가해 줄 주소를 작성해주었습니다.
이 때 같은 위치에 있는 views들을 가져오기 위해 from .import views를 했습니다.  #.과 import를 띄우지 않게 주의해야합니다!

django_pjt1/urls.py에서는 from django.urls import path 뒤에 include를 붙여주었고, community.urls 전체로 넘겨주기 위해
urlpatterns에 include()로 길을 내주었습니다.


5. View&Template
- base.html에 bootstrap에서 가져온 nav bar를 사용했습니다.

community 내 html 파일들에는 공통적으로 아래의 코드를 작성해주어 base.html의 기본 페이지 형식을 모든 url에 넘겨주었습니다.
{% extends 'base.html' %}
{% block content %}
{% endblock %}

- review_list.html
views에서 context에 key, value 값으로 주었던 reviews에서 for 문으로 리뷰 항목들을 한 세트씩 꺼내올 수 있게 했습니다.

- new_review.html
form 태그를 주어 create_review로 이동하게 했지만, 아마도 views에서 redirect를 주어 넘어가지 않는 것 같습니다.
method="GET"으로 여기에서 입력하는 title, content, rank를 submit 버튼을 눌렀을 때 저장되어 넘어가게 했습니다.
content는 <textarea></textarea>로 작성해 내용부분에는 길이가 긴 공백을 주었습니다.

-create_review,html
리뷰 작성 결과문을 작성했지만, 해당 페이지로 이동은 하지 않는 것 같습니다.

-views.py
review_list함수에는 return render로 해당 html 주로소 넘겨주고, creat_review함수에는 return redirec를 주어 해당 페이지로 바로 넘어갈 수 있게 했습니다.


*어려웠던 부분*
필수부분을 완성하는 것도 아직 익숙치 않아서 선택부분은 시도하지 못했던 점이 아쉽웠습니다.
계속 연습을 해 익숙하게 하는 것이 중요한 것 같습니다!