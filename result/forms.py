from django import forms
from django.core.exceptions import ValidationError
from .models import Result

class UploadFileForm(forms.Form):
    file = forms.FileField()


class ResultForm(forms.ModelForm):

    rank = forms.IntegerField(required=False)

    class Meta:
        model = Result
        exclude = ('publishedDate', )