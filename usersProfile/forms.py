from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import extendeduser, child


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = extendeduser
        fields = ['phone_num', 'location']


class StudentRegistrationForm1(forms.ModelForm):

    class Meta:
        model = child
        fields = ['child_name']
#        fields = ['child_name', 'age', 'gender',
#                  'age', 'date_of_birth', 'nationality']


class StudentRegistrationForm(forms.ModelForm):
    child_name = forms.CharField()

    class Meta:
        model = child
        fields = ('child_name', 'child_age', 'address',
                  'gender', 'date_of_birth', 'nationality')


class ChildProfileUpdateForm(forms.ModelForm):
    child_name = forms.CharField()

    class Meta:
        model = child
        fields = ['child_name', 'child_age', 'address',
                  'gender', 'date_of_birth', 'nationality']
