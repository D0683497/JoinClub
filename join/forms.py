from django import forms

LEVEL_CHOICES = (
    ('1', '大一'),
    ('2', '大二'),
    ('3', '大三'),
    ('4', '大四'),
    ('5', '碩一'),
    ('6', '碩二')
)

class JoinForm(forms.Form):
    name = forms.CharField(label='姓名', required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入姓名'}))
    nid = forms.CharField(label='學號', required=True, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入學號'}))
    dept = forms.CharField(label='系級', required=True, max_length=20, help_text="例如:資訊一甲", widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'deptHelp', 'placeholder': '請輸入系級'}))
    level = forms.ChoiceField(label='年級', choices=LEVEL_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': ''}))
    phone = forms.CharField(label='電話', required=True, max_length=15, help_text="請輸入可以聯絡到您的手機", widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'phoneHelp', 'placeholder': ''}))
    email = forms.EmailField(label='E-mail', required=True, help_text="請輸入您常用的 E-mail", widget=forms.EmailInput(attrs={'class': 'form-control', 'aria-describedby': 'emailHelp', 'placeholder': ''}))
