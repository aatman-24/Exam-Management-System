from django.shortcuts import render
from django.views.generic import View
from django import http
from .forms.exam_form import ExamForm
from .models import Exam
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime



# Create your views here.

def getExamBySlug(exam_slug):
    exam = Exam.objects.get(slug=exam_slug)
    if(exam is None):
        return "No Exam Found"
    return exam


class createExam(View):

    model = Exam
    form_class = ExamForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'examination/exam_form.html', {'form' :form})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newExam = bound_form.save()
            print(newExam)
            return redirect(newExam)
        else:
            return render(request, 'examination/exam_form.html', {'form':bound_form})


class getExam(View):

    model = Exam

    def get(self, request, exam_slug):
        exam = self.model.objects.get(slug=exam_slug)
        return render(request, 'examination/exam_detail.html', {'exam':exam})


class getExams(View):

    model = Exam
    exam_type = None

    def _getExam(self, filter):
        current_day = datetime.today()
        if(filter is None):
            return self.model.objects.all()
        elif(filter == "past"):
            return self.model.objects.filter(examDate__lt=current_day)
        elif(filter == "future"):
            return self.model.objects.filter(examDate__gte=current_day)
        return None

    def get(self, request):
        exams = self._getExam(self.exam_type)
        return render(request, 'examination/exam_list.html', {'exams':exams})


class deleteExam(View):
    model = Exam
    
    def get(self, request, exam_slug):
        exam = self.model.objects.get(slug=exam_slug)
        return render(request, 'examination/exam_confirm_delete.html', {'exam':exam})

    def post(self, request, exam_slug):
        exam = get_object_or_404(self.model, slug=exam_slug)
        exam.delete()
        return redirect('examination_exam_list')


    
class updateExam(View):

    model = Exam
    form_class = ExamForm

    def get(self, request, exam_slug):
        exam = self.model.objects.get(slug=exam_slug)
        form = self.form_class(instance=exam)
        return render(request, 'examination/exam_form_update.html', {'form':form, 'exam':exam})

    
    def post(self, request, exam_slug):
        exam = get_object_or_404(self.model, slug=exam_slug)
        bound_form = self.form_class(request.POST, instance = exam)
        if(bound_form.is_valid()):
            updatedExam = bound_form.save()
            messages.success(request, "Exam Updated")
            return redirect(updatedExam)
        return render(request, 'exam/exam_form_update.html', {'form':bound_form, 'exam':exam})
