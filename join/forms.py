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
    name = forms.CharField(label='姓名', required=True, max_length=50)
    nid = forms.CharField(label='學號', required=True, max_length=15)
    dept = forms.CharField(label='系級', required=True, max_length=20, help_text="例如:資訊一甲")
    level = forms.ChoiceField(label='年級', choices=LEVEL_CHOICES, required=True)
    phone = forms.CharField(label='電話', required=True, max_length=15, help_text="請輸入可以聯絡到您的手機")
    email = forms.EmailField(label='E-mail', required=True, help_text="請輸入您常用的 E-mail")
    privacy = forms.BooleanField(label='本人同意將個人資料提供逢甲大學黑客社使用，本社依個人資料保護法、相關法規及學校相關法規進行處理以及利用。', required=True)