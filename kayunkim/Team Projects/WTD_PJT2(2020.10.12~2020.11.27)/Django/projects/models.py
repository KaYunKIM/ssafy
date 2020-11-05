from django.db import models
from django import forms
from accounts.models import User

# Create your models here.
class Project(models.Model):  #각 프로젝트에 대한 정보
   title = models.CharField(max_length=20)
   deadline = models.DateField()
   members = models.ManyToManyField(User, through='Member') #Member가 Project와 User 사이의 중간 모델 역할

   def __str__(self):
      return self.title
    
class Member(models.Model):  #각 멤버에 대한 정보/ Project-Member(중간테이블)-User
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   role = models.CharField(max_length=20, default="general")  #녹음자/팀장/팀원

class Keyword(models.Model):
   title = models.CharField(max_length=20)

   def __str__(self):
      return self.title

class Meeting(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   title = models.CharField(max_length=20) 
   time = models.DateTimeField()
   origin_text = models.TextField(null=True)
   summary = models.TextField(null=True)
   keywords = models.ManyToManyField(Keyword, blank=True)  #Meeting/Keyword 어느쪽에서 선언해도 무방
   
   def __str__(self):
      return self.title

class Task(models.Model):
   meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
   title = models.CharField(max_length=1000)
   detail = models.TextField(default="", null=True)
   start_time = models.DateTimeField(null=True)
   end_time = models.DateTimeField(null=True)
   completed = models.BooleanField(default = False)
   manager = models.CharField(max_length=20, null=True)
   
   def __str__(self):
      return self.title

class Audio(models.Model): 
   audio = models.FileField(upload_to ='audio/', null=True) 