from django import forms
from django.contrib.auth.models import User
from django.db.models import Q
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


class StudentRegistrationForm(forms.ModelForm):
    child_name = forms.CharField()
    date_of_birth = forms.DateField(
        widget=forms.DateInput
        (attrs={'placeholder': 'MM/DD/YYYY'}))

    class Meta:
        model = child
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
        fields = ['child_name', 'address',
                  'gender', 'date_of_birth', 'nationality']


class ActivityCreationForm(forms.ModelForm):
    children_list = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=child.objects.all())
    teacher_list = User.objects.filter(is_staff=True)
    teacher_name = forms.ModelChoiceField(queryset=User.objects.filter(
        Q(is_staff=True) & Q(is_superuser=False)), empty_label="---------")
    activity_Date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'MM/DD/YYYY'}))

    class Meta:
        model = activity
        fields = ['teacher_name', 'children_list', 'activity_name', 'activity_description',
                  'activity_Date', 'activity_duration']
