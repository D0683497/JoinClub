from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Attend

class AttendForm(ModelForm):
    class Meta:
        model = Attend
        fields = ['name', 'nid']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入姓名'}),
            'nid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學號'})
        }
        labels = {
            'name': _('姓名'),
            'nid': _('學號'),
        }
        error_messages = {
            'name': {
                'required': _('必須填寫姓名'),
                'max_length': _('你的姓名太長囉'),
            },
            'nid': {
                'required': _('必須填寫學號'),
                'unique': _('您的學號已經被使用過囉'),
                'max_length': _('你的學號太長囉'),
            },
        }