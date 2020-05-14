from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    url =  models.TextField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=50)
    review =  models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)