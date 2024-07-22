from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AdmissionForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AdmissionFormForm(forms.ModelForm):
    class Meta:
        model = AdmissionForm
        fields = ['fullname', 'dob', 'address', 'school', 'qualification', 'photo', 'certificate', 'declaration']
