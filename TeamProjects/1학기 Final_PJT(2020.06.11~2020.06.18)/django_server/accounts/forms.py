from django import forms

class DateForm(forms.Form):
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d'])