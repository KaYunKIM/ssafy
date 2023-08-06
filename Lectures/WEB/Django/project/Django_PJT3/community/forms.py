from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    rank = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
            'max' : 5,
            'min' : 1,
            'step' : 1
            }
        )
    )
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']