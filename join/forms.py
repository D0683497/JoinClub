from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django .contrib.auth.forms import UsernameField
from django.core.exceptions import ValidationError

from .models import Member, Lesson

from tempus_dominus.widgets import DatePicker

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
    
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
                'required': _('請填寫您常用的電子信箱'), 
                'invalid': _('你的電子信箱看起來怪怪的'), 
                'max_length ': _('你的電子信箱太長囉'),
                'unique': _('您的電子信箱已經被使用囉'), 
            }, 
            'password': {
                'required': _('必須填寫密碼'),
                'max_length': _('你的密碼太長囉'),
            },
        }
   
class MemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['lesson'].required = True
    
    class Meta:
        model = Member
        fields = ['nid', 'sex', 'phone', 'birthday', 'lesson']
        widgets = {
            'nid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學號', 'aria-describedby': 'nidHelp'}), 
            'sex': forms.Select(attrs={'class': 'form-control'}), 
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入手機號碼'}), 
            'birthday': DatePicker(attrs={'append': 'fa fa-calendar'}, options={'locale': 'zh-tw', 'viewMode': 'years'}), 
            'lesson': forms.Select(attrs={'class': 'selectpicker show-tick form-control', 'data-live-search': 'true', 'aria-describedby': 'lessonHelp'}), 
        }
        labels = {
            'nid': _('學號'), 
            'sex': _('性別'), 
            'phone': _('手機號碼'), 
            'birthday': _('生日'), 
            'lesson': _('系級'), 
        }
        help_texts = {
            'nid': _('請填寫真實學號'),
            'lesson': _('若無您的系級，請洽工作人員或聯絡逢甲大學黑客社'), 
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
            'lesson': {
                'invalid': _('你的系級看起來怪怪的'), 
                'required': _('必須選擇您的系級'),
            },
        }

class ScanForm(forms.Form):
    nid         = forms.CharField(required=True, 
                    error_messages={'required': '此欄位必須填寫'}, 
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲查詢之學號'}),
                    label="學號")

class KeyinForm(forms.Form):
    nid         = forms.CharField(
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲查詢之學號'}),
                    required=False,
                    label="學號")
    email       = forms.EmailField(
                    widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲查詢之電子信箱'}),
                    required=False,
                    label="電子信箱")
    username    = forms.CharField(
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲查詢之帳號'}),
                    required=False,
                    label="帳號")
    first_name  = forms.CharField(
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲查詢之名字'}),
                    required=False,
                    label="名字")
    last_name   = forms.CharField(
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲查詢之姓氏'}),
                    required=False,
                    label="姓氏")
    phone       = forms.CharField(
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲查詢之手機號碼'}),
                    required=False,
                    label="手機號碼")
    lesson      = forms.ModelChoiceField(
                    widget=forms.Select(attrs={'class': 'selectpicker show-tick form-control', 'data-live-search': 'true'}), 
                    required=False,
                    queryset=Lesson.objects.all(),
                    label="系級")

class EditMemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditMemberForm, self).__init__(*args, **kwargs)
        self.fields['lesson'].required = True
        self.fields['status'].required = True
    
    class Meta:
        model = Member
        fields = ['nid', 'sex', 'phone', 'birthday', 'lesson', 'positions', 'status']
        widgets = {
            'nid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學號', 'aria-describedby': 'nidHelp'}), 
            'sex': forms.Select(attrs={'class': 'form-control'}), 
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入手機號碼'}), 
            'birthday': DatePicker(attrs={'append': 'fa fa-calendar'}, options={'locale': 'zh-tw', 'viewMode': 'years'}), 
            'lesson': forms.Select(attrs={'class': 'selectpicker show-tick form-control', 'data-live-search': 'true', 'aria-describedby': 'lessonHelp'}),
            'positions': forms.Select(attrs={'class': 'selectpicker show-tick form-control', 'data-live-search': 'true', 'aria-describedby': 'lessonHelp'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nid': _('學號'), 
            'sex': _('性別'), 
            'phone': _('手機號碼'), 
            'birthday': _('生日'), 
            'lesson': _('系級'), 
            'positions': _('職位'), 
            'status': _('狀態'),
        }
        help_texts = {
            'nid': _('請填寫真實學號'),
            'lesson': _('若無您的系級，請洽工作人員或聯絡逢甲大學黑客社'), 
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
            'lesson': {
                'invalid': _('你的系級看起來怪怪的'), 
                'required': _('必須選擇您的系級'),
            },
            'positions': {
                'invalid': _('你的職位看起來怪怪的'), 
            },
            'status': {
                'required': _('必須選擇狀態'),
                'invalid': _('你的狀態看起來怪怪的'), 
            },
        }

class EditUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入名字', 'aria-describedby': 'first_nameHelp'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入姓氏', 'aria-describedby': 'last_nameHelp'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '請輸入電子郵件', 'aria-describedby': 'emailHelp'}), 
        }
        labels = {
            'first_name': _('名字'), 
            'last_name': _('姓氏'), 
            'email': _('電子信箱'), 
        }
        help_texts = {
            'last_name': _('請填寫真實姓氏'),
            'first_name': _('請填寫真實名字'),
            'email': _('請填寫您常用的電子信箱'),
        }
        error_messages = {
            'first_name': {
                'required': _('請填寫真實名稱'), 
                'max_length': _('你的名字太長囉'), 
            }, 
            'last_name': {
                'required': _('請填寫真實姓氏'), 
                'max_length': _('你的姓氏太長囉'), 
            }, 
            'email': {
                'required': _('請填寫您常用的電子信箱'), 
                'invalid': _('你的電子信箱看起來怪怪的'), 
                'max_length ': _('你的電子信箱太長囉'),
            }, 
        }
