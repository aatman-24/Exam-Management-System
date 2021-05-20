from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import  View
from examination.models import Exam
from .models import Result
from .forms import UploadFileForm
from django.contrib.messages import success
from .utils import makeResult
from .forms import ResultForm
from django.shortcuts import get_object_or_404, redirect
from student.models import Student
from django.contrib import messages

def handle_uploaded_file(f, fname):
    with open(f'store/{fname}.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
class UploadResultFile(View):

    def get(self, request, exam_slug):
        exam = Exam.objects.get(slug = exam_slug)
        form = UploadFileForm()
        return render(request, 'result/upload.html', {'exam':exam, 'form':form})

    def post(self, request, exam_slug):
        form = UploadFileForm(request.POST, request.FILES)
        exam = Exam.objects.get(slug = exam_slug)
        if form.is_valid():
            x = request.FILES['file']
            fname = str(exam.id) + "_" + exam.examName + "_" + str(exam.examDate)
            handle_uploaded_file(request.FILES['file'], fname)
            success(request, "File is uploaded")
            
            makeResult(f"store/{fname}.xlsx")

            #TODO : WHAT I GO FORM HERE ?
            exam.resultPublished = True
            return HttpResponse("Success")
        return render(request, 'result/okay.html', {'form': form})

class GetResult(View):

    model = Result

    def get(self, request, result_slug):
        result = self.model.objects.get(slug=result_slug)
        return render(request, 'result/result_detail.html', {'exam' : result.exam, 'result':result})
        

class CreateResult(View):

    model = Result
    form = ResultForm

    def get(self, request, student_slug, exam_slug):
        student = Student.objects.get(slug=student_slug)
        exam = Exam.objects.get(slug=exam_slug)
        form =  self.form_class(initial={'student':student, 'exam':exam})
        return render(request, 'result/result_form.html', {'form':form})

    def post(self, request, student_slug, exam_slug):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newResult = bound_form.save(request)
            print(newResult)
            return redirect(newResult)
        else:
            return render(request, 'result/result.html', {'form':bound_form})

class UpdateResult(View):

    model = Result
    form_class = ResultForm

    def get(self, request, result_slug):
        result = self.model.objects.get(slug=result_slug)
        form = self.form_class(instance=result)
        return render(request, 'result/result_form_update.html', {'form':form, 'result': result})


    def post(self, request, result_slug):
        result = get_object_or_404(self.model, slug=result_slug)
        bound_form = self.form_class(request.POST, instance = result)
        if(bound_form.is_valid()):
            updatedExam = bound_form.save()
            messages.success(request, "Exam Updated")
            return redirect(updatedExam)
        return render(request, 'result/result_form_update.html' , {'form':bound_form, 'result': result})


class DeleteResult(View):

    model = Result

    def get(self, request, result_slug):
        result = self.model.objects.get(slug=result_slug)
        return render(request, 'result/result_confirm_delete.html', {'result': result})


    def post(self, request, result_slug):
        result = get_object_or_404(self.model, slug=result_slug)
        result.delete()
        return redirect('examination_exam_list')