from django import forms
from .models import Poll, Choice, Comment

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['Title','IssueA', 'IssueB',]

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['select',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']