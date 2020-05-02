from django.contrib import admin

# Register your models here.
from .models import Poll, Comment, Choice

admin.site.register(Poll)
admin.site.register(Comment)
admin.site.register(Choice)