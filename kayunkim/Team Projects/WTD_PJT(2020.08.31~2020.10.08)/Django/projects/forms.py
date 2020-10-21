from django import forms

class AudioFileForm(forms.Form):
    audio = forms.FileField(label="Select a File" , help_text="max. 42 megabytes")