from .models import Student, Profile, ParentProfile
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator 
from utils.util import SlugCleanMixin

class StudentForm(forms.ModelForm, SlugCleanMixin):

    std = forms.IntegerField(max_value=12, min_value=11)
    class Meta:
        model = Student
        exclude = ('user',)


class StudentProfileForm(forms.ModelForm, SlugCleanMixin):

    class Meta:
        model = Profile
        exclude = ('student',)


class ParentProfileForm(forms.ModelForm, SlugCleanMixin):

    class Meta:
        model = ParentProfile
        exclude = ('student',)
        

    