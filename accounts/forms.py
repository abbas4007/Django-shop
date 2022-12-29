from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

class UserLoginForm(forms.Form):
	phone = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class VerifyCodeForm(forms.Form):
	code = forms.IntegerField()