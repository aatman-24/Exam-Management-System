from django import forms
from ..models import Exam
from django.core.exceptions import ValidationError
from student.forms import SlugCleanMixin

class ExamForm(forms.ModelForm, SlugCleanMixin):

    class Meta:
        model = Exam
        fields = '__all__'

