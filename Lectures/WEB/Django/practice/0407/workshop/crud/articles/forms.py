from django import forms
from .models import Article
# from crispy_forms.helper import FormHelper
# from cistpy_forms.layout import Submit


class ArticleForm(forms.ModelForm):

    class Meta:  #django에서 정해놓은 것
        model = Article
        fields = '__all__'  #title,content포함