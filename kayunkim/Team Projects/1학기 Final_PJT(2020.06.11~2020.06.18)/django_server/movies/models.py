from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    original_title = models.TextField()
    genre = models.TextField()
    director = models.TextField()
    actors = models.TextField()
    poster_url = models.TextField()
    backdrop_url = models.TextField()
    overview = models.TextField()
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    trailer_url = models.TextField()
    release_date = models.DateField()
    runtime = models.IntegerField()
    language = models.TextField()
    keywords = models.TextField()
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies')

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])