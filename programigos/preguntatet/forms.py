from django.contrib.auth.models import User
from django import forms

class guardar(forms.ModelForm):
	title = forms.CharField(max_length=100)
	url = forms.URLField()#campo de tipo url
	content = forms.CharField(widget=forms.Textarea)