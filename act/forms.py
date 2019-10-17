from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from tempus_dominus.widgets import DatePicker, TimePicker
from django.core.exceptions import ValidationError

from .models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'startdate', 'endtdate', 'starttime', 'endtime', 'teachers', 'signup', 'locations', 'intro', 'other', 'status', 'categorys']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入名稱', 'aria-describedby': 'usernameHelp'}), 
            'startdate': DatePicker(attrs={'append': 'fa fa-calendar'}, options={'locale': 'zh-tw', 'viewMode': 'years'}),
            'endtdate': DatePicker(attrs={'append': 'fa fa-calendar'}, options={'locale': 'zh-tw', 'viewMode': 'years'}),
            'starttime': TimePicker(attrs={'append': 'far fa-clock'}, options={'locale': 'zh-tw', 'format': 'HH:mm'}),
            'endtime': TimePicker(attrs={'append': 'far fa-clock'}, options={'locale': 'zh-tw', 'format': 'HH:mm'}),
            'teachers': forms.SelectMultiple(attrs={'class': 'selectpicker form-control'}),
            'signup': forms.URLInput(attrs={'class': 'form-control', 'placeholder': '請輸入報名連結'}),
            'locations': forms.Select(attrs={'class': 'selectpicker show-tick form-control', 'data-live-search': 'true'}),
            'intro': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '請輸入簡介'}),
            'other': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '請輸入其他', 'aria-describedby': 'otherHelp'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'categorys': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': _('名稱'), 
            'startdate': _('開始日期'), 
            'endtdate': _('結束日期'), 
            'starttime': _('開始時間'), 
            'endtime': _('結束時間'), 
            'teachers': _('講師'),  
            'signup': _('報名連結'), 
            'locations': _('地點'), 
            'intro': _('簡介'), 
            'other': _('其他'), 
            'status': _('狀態'), 
            'categorys': _('類別'),
        }
        help_texts = {
            'other': _('補充事項'),
        }
        error_messages = {
            'name': {
                'required': _('必須填寫名稱'),
                'unique': _('這個名稱以經被使用了'),
                'max_length': _('名稱太長了'),
            }, 
            'startdate': {
                'required': _('必須要有開始日期'),
                'invalid': _('你的開始日期看起來怪怪的'),
            }, 
            'endtdate': {
                'required': _('必須要有結束日期'),
                'invalid': _('你的結束日期看起來怪怪的'),
            }, 
            'starttime': {
                'required': _('必須要有開始時間'),
                'invalid': _('你的開始時間看起來怪怪的'),
            }, 
            'endtime': {
                'required': _('必須要有結束時間'),
                'invalid': _('你的結束時間看起來怪怪的'),
            }, 
            'teachers': {
                'required': _('必須填寫講師'),
            }, 
            'signup': {
                'max_length': _('報名網址太長了'),
                'invalid': _('報名網址看起來怪怪的'),
            }, 
            'locations': {
                'required': _('必須填寫地點'),
            }, 
            'intro': {

            }, 
            'other': {

            }, 
            'status': {
                'required': _('必須選擇狀態'),
                'invalid': _('你的狀態看起來怪怪的'),
            }, 
            'categorys': {

            }, 
        }

