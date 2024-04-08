from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProjectCreate
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CreateProject(forms.ModelForm):
    class Meta:
        model = ProjectCreate
        fields = ('title', 'des', 'startdate', 'enddate', 'owner')