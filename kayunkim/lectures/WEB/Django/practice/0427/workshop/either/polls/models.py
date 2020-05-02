from django.db import models

# Create your models here.
class Theme(models.Model):
    name = models.TextField()

class Poll(models.Model):
    Title = models.CharField(max_length=100)
    IssueA = models.CharField(max_length=20)
    IssueB = models.CharField(max_length=20)
    IssueA_count = models.IntegerField(default=0)
    IssueB_count = models.IntegerField(default=0)
    # theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

class Choice(models.Model):
    select = models.CharField(max_length=20)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

class Comment(models.Model):
    pick = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
