from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from tempus_dominus.widgets import DatePicker, TimePicker
from django.core.exceptions import ValidationError
from tempus_dominus.widgets import DatePicker
from django.contrib.auth.models import User
from django .contrib.auth.forms import UsernameField

from .models import Teacher, Location, Category
from join.models import Degree, College, Department, Lesson
from join.models import Attendee

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'job', 'exp', 'other']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入名字'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入姓氏'}), 
            'job': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '請輸入現職'}),
            'exp': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '請輸入學經歷',}),
            'other': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '請輸入其他'}),
        }
        labels = {
            'first_name': _('名字'), 
            'last_name': _('姓氏'), 
            'job': _('現職'), 
            'exp': _('學經歷'), 
            'other': _('其他'), 
        }
        error_messages = {
            'first_name': {
                'required': _('必須填寫名字'),
                'max_length': _('名字太長了'),
            }, 
            'first_name': {
                'required': _('必須填寫姓氏'),
                'max_length': _('姓氏太長了'),
            }, 
        }

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'way']
        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '請輸入名稱'}),
            'way': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '請輸入路徑',}),
        }
        labels = {
            'name': _('名稱'), 
            'way': _('路徑'), 
        }
        error_messages = {
            'name': {
                'required': _('必須填寫名稱'),
            }, 
            'way': {
            }, 
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入名稱'}), 
        }
        labels = {
            'name': _('名稱'), 
        }
        error_messages = {
            'name': {
                'required': _('必須填寫名稱'),
                'max_length': _('名稱太長了'),
                'unique': _('這個類別已經有了'),
            }, 
        }

class DegreeForm(ModelForm):
    class Meta:
        model = Degree
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學制'}), 
        }
        labels = {
            'name': _('學制'), 
        }
        error_messages = {
            'name': {
                'required': _('必須填寫學制'),
                'max_length': _('學制太長了'),
            }, 
        }

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = ['name', 'degree']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學院'}), 
            'degree': forms.Select(attrs={'class': 'selectpicker show-tick form-control', 'data-live-search': 'true'}),
        }
        labels = {
            'name': _('學院'),
            'degree': _('學制'),
        }
        error_messages = {
            'name': {
                'required': _('必須填寫學院'),
                'max_length': _('學院太長了'),
            }, 
            'degree': {
                'required': _('必須選擇學制'),
                'invalid': _('你的學制看起來怪怪的'),
            },
        }

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'college']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學系'}), 
            'college': forms.Select(attrs={'class': 'selectpicker show-tick form-control', 'data-live-search': 'true'}),
        }
        labels = {
            'name': _('學系'), 
            'college': _('學院'),
        }
        error_messages = {
            'name': {
                'required': _('必須填寫學系'),
                'max_length': _('學系太長了'),
            }, 
            'college': {
                'required': _('必須選擇學院'),
                'invalid': _('你的學院看起來怪怪的'),
            },
        }

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入班級'}), 
            'department': forms.Select(attrs={'class': 'selectpicker show-tick form-control', 'data-live-search': 'true'}),
        }
        labels = {
            'name': _('班級'), 
            'department': _('學系'),
        }
        error_messages = {
            'name': {
                'required': _('必須填寫班級'),
                'max_length': _('班級太長了'),
            }, 
            'department': {
                'required': _('必須選擇學系'),
                'invalid': _('你的學系看起來怪怪的'),
            },
        }

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 7:
            raise ValidationError(_('你的密碼至少須 8 個字'),)
        if password.isdigit():
            raise ValidationError(_("你的密碼不能都是數字"),)
        return password

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("您的電子信箱已經被使用囉"),)
        return email

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        field_classes = {
            'username': UsernameField,
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入帳號', 'aria-describedby': 'usernameHelp'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入名字', 'aria-describedby': 'first_nameHelp'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入姓氏', 'aria-describedby': 'last_nameHelp'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '請輸入電子郵件', 'aria-describedby': 'emailHelp'}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '請輸入密碼', 'aria-describedby': 'passwordHelp'}), 
        }
        labels = {
            'username': _('帳號'), 
            'first_name': _('名字'), 
            'last_name': _('姓氏'), 
            'email': _('電子信箱'), 
            'password': _('密碼'), 
        }
        help_texts = {
            'username': _('此帳號為之後登入本網站所需'),
            'last_name': _('請填寫真實姓氏'),
            'first_name': _('請填寫真實名字'),
            'email': _('請填寫您常用的電子信箱'),
            'password': _('此密碼為之後登入本網站所需'), 
        }
        error_messages = {
            'username': {
                'unique': _('您的帳號已經被使用過囉'), 
                'required': _('必須填寫帳號'), 
                'max_length': _('你的帳號太長囉'), 
                'invalid': _('帳號只能包含字母、數字和 @/./+/-/_'), 
            }, 
            'first_name': {
                'required': _('請填寫真實名稱'), 
                'max_length': _('你的名字太長囉'), 
            }, 
            'last_name': {
                'required': _('請填寫真實姓氏'), 
                'max_length': _('你的姓氏太長囉'), 
            }, 
            'email': {
                'invalid': _('你的電子信箱看起來怪怪的'), 
                'max_length ': _('你的電子信箱太長囉'),
                'unique': _('您的電子信箱已經被使用囉'), 
            }, 
            'password': {
                'required': _('必須填寫密碼'),
                'max_length': _('你的密碼太長囉'),
            },
        }

class AttendeeForm(ModelForm):
    class Meta:
        model = Attendee
        fields = ['nid', 'sex', 'phone', 'birthday', 'job']
        widgets = {
            'nid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學號', 'aria-describedby': 'nidHelp'}), 
            'sex': forms.Select(attrs={'class': 'form-control'}), 
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入手機號碼'}), 
            'birthday': DatePicker(attrs={'append': 'fa fa-calendar'}, options={'locale': 'zh-tw', 'viewMode': 'years'}), 
            'job': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入現職'}), 
        }
        labels = {
            'nid': _('學號'), 
            'sex': _('性別'), 
            'phone': _('手機號碼'), 
            'birthday': _('生日'), 
            'job': _('現職'), 
        }
        help_texts = {
            'nid': _('請填寫真實學號'),
        }
        error_messages = {
            'nid': {
                'unique': _('您的學號已經被使用過囉'),
                'required': _('必須填寫學號'), 
                'max_length': _('你的學號太長囉'),
            }, 
            'sex': {
                'invalid': _('你的性別看起來怪怪的'),
            }, 
            'phone': {
                'unique': _('您的手機號碼已經被使用過囉'),
                'max_length': _('你的手機號碼太長囉'), 
            }, 
            'birthday': {
                'invalid': _('你的生日看起來怪怪的'),
            }, 
            'job': {
                'max_length': _('你的現職太長囉'),
            },
        }
