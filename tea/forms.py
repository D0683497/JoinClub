from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Tea

class TeaForm(ModelForm):
    class Meta:
        model = Tea
        fields = ['nid', 'first_name', 'last_name']
        widgets = {
            'nid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學號'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入您的姓氏'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入您的名字'}),
        }
        labels = {
            'nid': _('學號'),
            'last_name': _('姓氏'),
            'first_name': _('名字'),
        }
        help_texts = {
            'nid': _('請填寫真實學號'),
            'last_name': _('請填寫真實姓氏'),
            'first_name': _('請填寫真實名字'),
        }
        error_messages = {
            'nid': {
                'unique': _('您的學號已經被使用過囉'),
                'required': _('必須填寫學號'),
                'max_length': _('你的學號太長囉'),
            },
            'last_name': {
                'required': _('請填寫真實姓氏'),
                'max_length': _('你的姓氏太長囉'),
            },
            'first_name': {
                'required': _('請填寫真實名稱'),
                'max_length': _('你的名字太長囉'),
            },
        }

class CheckinForm(forms.Form):
    nid = forms.CharField(required=True, 
        error_messages={'required': '此欄位必須填寫'}, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲查詢之學號'}),
        label="學號")

class EditForm(ModelForm):
    class Meta:
        model = Tea
        fields = ['nid', 'first_name', 'last_name', 'status']
        widgets = {
            'nid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學號'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入您的姓氏'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入您的名字'}),
            'status': forms.SelectMultiple(attrs={'class': 'selectpicker form-control'}),
        }
        labels = {
            'nid': _('學號'),
            'last_name': _('姓氏'),
            'first_name': _('名字'),
            'status':_('狀態'),
        }
        help_texts = {
            'nid': _('請填寫真實學號'),
            'last_name': _('請填寫真實姓氏'),
            'first_name': _('請填寫真實名字'),
            'status':_('這是多選喔'),
        }
        error_messages = {
            'nid': {
                'unique': _('您的學號已經被使用過囉'),
                'required': _('必須填寫學號'),
                'max_length': _('你的學號太長囉'),
            },
            'last_name': {
                'required': _('請填寫真實姓氏'),
                'max_length': _('你的姓氏太長囉'),
            },
            'first_name': {
                'required': _('請填寫真實名稱'),
                'max_length': _('你的名字太長囉'),
            },
        }
