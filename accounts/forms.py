from django import forms
from django.contrib.auth.models import User
from .models import Profile

class EditUserform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control", "placeholder": "Имя"}),
            "last_name":forms.TextInput(attrs={"class":"form-control", "placeholder": "Фамилия"}),
            "username":forms.TextInput(attrs={"class":"form-control", "placeholder": "Имя пользователя"}),
            "email":forms.EmailInput(attrs={"class":"form-control", "placeholder": "Эл. почта"}),
            "password":forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Пароль"})
        }
        
class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']