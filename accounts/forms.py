from django.forms import ModelForm
from accounts.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        widgets = {
                  'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
                  'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
                  'birth_date': forms.DateInput(attrs={'placeholder': 'Birth date'}),
                  'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
                  'username': forms.TextInput(attrs={'placeholder': 'Username'}),
                  'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
                  'password2': forms.PasswordInput(attrs={'placeholder': 'Verify password'}),

                  }

        fields = ['first_name','last_name','birth_date','email','username','password1','password2','is_active']


    def __init__(self, *args, **kwargs):

        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={ 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password confirmation'})



    # def clean_birth_date(self, *args, **kwargs):
    #     birth_date = self.cleaned_data.get()
    #     if birth_date


    # def clean_is_active(self, *args, **kwargs):
    #     is_active = self.cleaned_data['is_active']
    #     if is_active == False:
    #         raise ValidationError("User didn't accept the terms and conditions!")
    #     return is_active

class User_complete(ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name','last_name','is_active']