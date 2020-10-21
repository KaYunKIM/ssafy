from django.db import models
from accounts.models import User

# Create your models here.
class Schedule(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=20)
	detail = models.TextField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()

	def __str__(self):
		return self.title
