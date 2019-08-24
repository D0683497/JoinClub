from django import forms
from django.core.exceptions import ValidationError
from .models import Member
import re

LEVEL_CHOICES = (
    ('B1', '大一'),
    ('B2', '大二'),
    ('B3', '大三'),
    ('B4', '大四'),
    ('M1', '碩一'),
    ('M2', '碩二')
)

class JoinForm(forms.Form):
    name  = forms.CharField(label='姓名', 
                            required=True, 
                            max_length=50, 
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入姓名'}), 
                            error_messages={'required': '必須填寫姓名', 'max_length': '你的姓名太長囉'})
    nid   = forms.CharField(label='學號', 
                            required=True, 
                            max_length=15, 
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學號'}), 
                            error_messages={'required': '必須填寫學號', 'max_length': '你的學號太長囉'})
    dept  = forms.CharField(label='系級', 
                            required=True, 
                            max_length=20, 
                            help_text="例如:資訊一甲", 
                            widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'deptHelp', 'placeholder': '請輸入系級'}), 
                            error_messages={'required': '必須填寫系級', 'max_length': '你的系級太長囉'})
    level = forms.ChoiceField(label='年級', 
                            choices=LEVEL_CHOICES, 
                            required=True, 
                            widget=forms.Select(attrs={'class': 'form-control', 'placeholder': ''}), 
                            error_messages={'required': '必須選擇年級', 'invalid_choice': '請勿亂來'})
    phone = forms.CharField(label='電話', 
                            required=True, 
                            max_length=15, 
                            help_text="請輸入可以聯絡到您的手機", 
                            widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'phoneHelp', 'placeholder': '請輸入電話號碼'}), 
                            error_messages={'required': '必須填寫電話', 'max_length': '你的電話太長囉'})
    email = forms.EmailField(label='E-mail', 
                            required=True, 
                            help_text="請輸入您常用的 E-mail", 
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'aria-describedby': 'emailHelp', 'placeholder': '請輸入點子郵件'}), 
                            error_messages={'required': '必須填寫 E-mail', 'invalid': '您的 E-mail 看起來怪怪的喔'})
    
    #驗證 nid 是否重複
    def clean_nid(self):
        nid = self.cleaned_data['nid']
        if Member.objects.filter(nid=nid).exists():
            raise ValidationError("您的學號已經被使用過囉")
        return nid
    
    #驗證 phone 是否重複
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if Member.objects.filter(phone=phone).exists():
            raise ValidationError("您的手機號碼已經被使用過囉")
        return phone

    #驗證 email 是否重複
    def clean_email(self):
        email = self.cleaned_data['email']
        if Member.objects.filter(email=email).exists():
            raise ValidationError("您的 Email 已經被使用過囉")
        return email
