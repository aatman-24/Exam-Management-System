from django import forms
from django.core.exceptions import ValidationError 
from .models import Subject
from utils.util import SlugCleanMixin


class SubjectForm(forms.ModelForm, SlugCleanMixin):

    standard = forms.IntegerField(max_value=12, min_value=11)

    class Meta:

        model = Subject
        exclude = ('totalMarks', 'totalExam', 'currentYear')
