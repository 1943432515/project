from captcha.fields import CaptchaField
from django import forms

class loginform(forms.Form):
    username=forms.CharField(label="用户名",required=True)
    password=forms.CharField(label="密码", required=True)
    captcha=CaptchaField()
