from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'description',)

admin.site.register(Movie, MovieAdmin)