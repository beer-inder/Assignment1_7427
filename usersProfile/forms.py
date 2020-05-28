from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import extendeduser, child, guardian, activity


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
#        fields = ('child_name', 'child_age', 'address',
#                  'gender', 'date_of_birth', 'nationality')
        fields = ('child_name', 'address',
                  'gender', 'date_of_birth', 'nationality')


class GuardianRegisterForm(forms.ModelForm):
    class Meta:
        model = guardian
        fields = ['guardian_name', 'relation_guardian', 'phone_num']


class ChildProfileUpdateForm(forms.ModelForm):
    child_name = forms.CharField()

    class Meta:
        model = child
#        fields = ['child_name', 'child_age', 'address',
#                  'gender', 'date_of_birth', 'nationality']
        fields = ['child_name', 'address',
                  'gender', 'date_of_birth', 'nationality']


class ActivityCreationForm(forms.ModelForm):
    children_list = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=child.objects.all())
    teacher_list = User.objects.filter(is_staff=True)
    teacher_name = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=True), empty_label="---------")

    class Meta:
        model = activity
        fields = ['teacher_name', 'children_list', 'activity_name', 'activity_description',
                  'activity_DateTime', 'activity_duration']
