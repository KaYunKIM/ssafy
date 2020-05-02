from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#상속=>custom
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  #accounts.User
        fields= ['username',]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email']