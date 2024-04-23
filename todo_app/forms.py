from django import forms
from .models import TodoModel


class AddTodoForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Enter Task Name'}))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'placeholder':'Enter Task description'}), required=False)