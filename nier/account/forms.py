from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, error_messages={'required':'用户名不能为空'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'密码不能为空'})
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(error_messages={'required': 'email不能为空'})

    def clean_username(self):
        username = self.cleaned_data.get('username','')
        if len(username) < 6 or len(username) > 18:
            raise forms.ValidationError('用户名必须6-18个字符')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('已经存在该用户')
        except ObjectDoesNotExist as e:
            pass
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password','')
        if len(password) < 6 or len(password) > 18:
            raise forms.ValidationError('密码必须6-18个字符')
        return password

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2', '')
        # get password from origin form.data, not from cleand_password
        password = self.data.get('password')
        if password2 != password:
            raise forms.ValidationError('两次输入密码结果不一致')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email','')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError('该邮箱已被注册')
        except ObjectDoesNotExist as e:
            pass
        return email

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, error_messages={'required':'用户名不能为空'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'密码不能为空'})

    def clean_username(self):
        username = self.cleaned_data.get('username','')
        try:
            login_user = User.objects.get(username=username)
            if login_user.userinfo.status == 2:
                raise forms.ValidationError('bee band contant admin')
            else:
                return username
        except ObjectDoesNotExist as e:
            raise forms.ValidationError('auth faild')


    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        return password

class AccountInfoForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    role = forms.IntegerField()
    group = forms.CharField()
    createtime = forms.DateTimeField()
    logintime = forms.DateTimeField()
    status = forms.IntegerField()
    message = forms.CharField()