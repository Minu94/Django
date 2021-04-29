from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Profile
from django.db.models import Q


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        try:
            object = User.objects.get(email=email)
            if (object):
                msg = "email already exists"
                self.add_error('email',msg)

        except Exception as e:
            pass


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


class CreateProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['user','profile_pic','bio','birth_date']
        widgets = {'birth_date':forms.DateInput(),'user':forms.HiddenInput()
        }




