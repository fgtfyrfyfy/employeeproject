from .models import employee
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForms(ModelForm):
    class Meta:
        model=employee
        fields='__all__'

class AdminForms(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password']