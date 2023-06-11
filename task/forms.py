from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class UserCustomCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserCustomChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'created_by', 'assigned_to', 'due_date']