from .models import Student, Profile, ParentProfile
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator 


class SlugCleanMixin:
    ''' Mixin class for slug cleaning method '''
    def clean_slug(self):       # both TagForm and StartupForm both contain this method.
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create' or new_slug == 'list' :
            raise ValidationError('Slug may not be "create".')
        return new_slug

class StudentForm(forms.ModelForm, SlugCleanMixin):

    
    std = forms.IntegerField(max_value=12, min_value=11)

    class Meta:
        model = Student
        fields = '__all__'


class StudentProfileForm(forms.ModelForm, SlugCleanMixin):

    class Meta:
        model = Profile
        exclude = ('student',)


class ParentProfileForm(forms.ModelForm, SlugCleanMixin):

    class Meta:
        model = ParentProfile
        exclude = ('student',)
        

    