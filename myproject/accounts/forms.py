from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
   # username = forms.Field(widget=forms.TextInput(attrs={'class':'form-control'}))
   # email = forms.Field(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)
    password2 = forms.CharField(label="تکرار رمز  عبور", widget=forms.PasswordInput)


    email = forms.EmailField(max_length=254, required=True, label="ایمیل" )

    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username': 'نام کاربری',
            'last_name': 'نام ',
            'email': 'ایمیل',
            'password1': 'رمز عبور',
            'password2': 'تکرار رمز عبور',
        }
        help_texts = {
            'username': None,
          #  'email': None,
           # 'password1': None,
            #'password2': None,

        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('کاربری با ایمیل وارد شده وجود دارد')
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('کاربری با نام کاربری وارد شده وجود دارد')
        return username

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if password1 != password2:
            raise forms.ValidationError('گذرواژه و تکرار گذرواژه یکسان نیستند')
        return password1

    def save(self, commit=True):
        super(SignUpForm, self).save(commit)


