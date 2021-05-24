from django import forms
from ..models import Exam
from django.core.exceptions import ValidationError
from student.forms import SlugCleanMixin
from study.models import Subject
from datetime import datetime

class ExamForm(forms.ModelForm, SlugCleanMixin):

    def __init__(self,*args,**kwargs):
        super(ExamForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['subject'].queryset = Subject.objects.filter(currentYear__year=datetime.now().year)
    class Meta:
        model = Exam
        fields = '__all__'

