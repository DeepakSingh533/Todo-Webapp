from django import forms
from .models import *

class TodoForm(forms.Form):
	text = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder' :'Write your Todo here'}))

