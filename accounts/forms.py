from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='이름')
    email = forms.CharField(label='이메일')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("비밀번호가 틀립니다.")
        return cd['password2']
