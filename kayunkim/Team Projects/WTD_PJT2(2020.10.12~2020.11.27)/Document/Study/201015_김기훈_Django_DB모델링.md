모델 내 데이터필드 

GENDER_CHOICES = [
  ('M' , 'Male'),
  ('F' , 'Female'),
] //이렇게 값 선택하게 가능.

models.CharField(blank=True, max_length=255)
models.ImageField(blank=True)
models.URLField(blank=True)
models.CharField(blank=True, choices=GENDER_CHOICED, max_length=255)
models.ManyToManyField("self") --> 이안의값 외래키

class TimeStampModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    abstract = True //이 옵션을 주면 단독으로 테이블 만들어지지 않음.

class Post(TimeStampModel) : //상속해주기
  author = models.ForeignKey(
		user_model.User, //위에 임포트해줘야함.
		null=True,
		on_delete=models.CASCADE,
		) //외래키 설정
  
  image_likes = models.ManyToManyField(user_model.User)

모델만들고 
makemigrations --> 명세서를 만든다는 느낌.
migrate --> 쟝고 내 디비 테이블을 만듬. 

