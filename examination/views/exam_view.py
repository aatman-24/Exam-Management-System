from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django import http
from django.contrib import messages
from datetime import datetime
from django.utils.decorators import method_decorator
from users.decorator import class_login_required, class_require_authenticated_permisssion, class_login_required
from result.models import Result
from study.views import updateExamRecord, deleteExamRecord
from ..forms import ExamForm
from ..models import Exam


# Create your views here.

def GetExamBySlug(exam_slug):
    exam = Exam.objects.get(slug=exam_slug)
    if(exam is None):
        return "No Exam Found"
    return exam

@class_require_authenticated_permisssion('examination.publish_exam')
class CreateExam(View):

    model = Exam
    form_class = ExamForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'examination/exam_form.html', {'form' :form})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newExam = bound_form.save()
            updateExamRecord(newExam)
            return redirect(newExam)
        else:
            return render(request, 'examination/exam_form.html', {'form':bound_form})


@class_login_required
class GetExam(View):

    model = Exam

    def get(self, request, exam_slug):
        exam = self.model.objects.get(slug=exam_slug)
        return render(request, 'examination/exam_detail.html', {'exam':exam})

@class_login_required
class GetExams(View):

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

@class_require_authenticated_permisssion('examination.publish_exam')
class DeleteExam(View):
    model = Exam
    
    def get(self, request, exam_slug):
        exam = self.model.objects.get(slug=exam_slug)
        return render(request, 'examination/exam_confirm_delete.html', {'exam':exam})

    def post(self, request, exam_slug):
        exam = get_object_or_404(self.model, slug=exam_slug)
        deleteExamRecord(exam)
        exam.delete()
        return redirect('examination_exam_list')


@class_require_authenticated_permisssion('examination.publish_exam')
class UpdateExam(View):

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

class GetExamResult(View):

    model = Exam

    def get(self, request, exam_slug):
        exam = get_object_or_404(self.model, slug=exam_slug)
        results = exam.result.all()
        return render(request, 'examination/exam_result_list.html', {'exam': exam, 'results': results})
