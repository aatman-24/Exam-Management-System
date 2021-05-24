from django.shortcuts import render
from django.views.generic import View
from django import http
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from ..forms import SubjectForm
from ..models import Subject, SubjectExamRecord
from datetime import datetime



class createSubject(View):

    model = Subject
    form_class = SubjectForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'study/subject_form.html' , {'form':form})
    
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newSubject = bound_form.save()
            addExamRecord(newSubject)
            return redirect(newSubject)
        else:
            return render(request, 'study/subject_form.html' , {'form':bound_form})

class getSubject(View):

    model = Subject

    def get(self, request, subject_slug):
        subject = get_object_or_404(self.model, slug=subject_slug)
        return render(request, 'study/subject_detail.html', {'subject': subject})


class getSubjects(View):

    model = Subject
    this_year = True

    def get(self, request):
        if(self.this_year):
            subjects = self.model.objects.get(currentYear__year=datetime.now().year)
        else:
            subjects = self.model.objects.filter()
        return render(request, 'study/subject_list.html', {'subjects': subjects})


class deleteSubject(View):

    model = Subject

    def get(self, request, subject_slug):
        subject = self.model.objects.get(slug=subject_slug)
        return render(request, 'study/subject_confirm_delete.html', {'subject': subject})

    
    def post(self, request, subject_slug):
        subject = get_object_or_404(self.model, slug=subject_slug)
        subject.delete()
        return redirect('study_subject_curYearList')


class updatesubject(View):

    model = Subject
    form_class = SubjectForm

    
    def get(self, request, subject_slug):
        subject = self.model.objects.get(slug=subject_slug)
        subjectForm = self.form_class(instance=subject)
        return render(request, 'study/subject_form_update.html', {'form': subjectForm, 'subject' : subject})

    def post(self, request, subject_slug):
        subject = get_object_or_404(self.model, slug=subject_slug)
        bound_form = self.form_class(request.POST, instance=subject)
        if(bound_form.is_valid()):
            updated_subject = bound_form.save()
            messages.success(request, "Subject is Updated!")
            return redirect(updated_subject)
        return render(request, 'study/subject_form_update.html', {'form': bound_form, 'subject' : subject})

