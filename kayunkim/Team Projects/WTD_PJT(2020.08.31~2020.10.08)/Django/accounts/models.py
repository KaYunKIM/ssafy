from django.db import models

# Create your models here.
class User(models.Model):
	email= models.CharField(max_length=50)
	platform = models.CharField(max_length=10)
	nickname= models.CharField(max_length=20)
	position= models.CharField(max_length=20)