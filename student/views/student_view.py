from django.shortcuts import render
from django.views.generic import View
from django import http
from ..forms import StudentForm
from ..models import Student
from ..utils import pick
from django.template.context_processors import csrf
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

def getStudentBySlug(student_slug):
    student = Student.objects.get(slug=student_slug)
    if(student is None):
        return "No Student Found"
    return student

class studentCreate(View):

    model = Student
    form_class = StudentForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'student/student_form.html' , {'form':form})
    
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newStudent = bound_form.save()
            return redirect(newStudent)
        else:
            return render(request, 'student/student_form.html' , {'form':bound_form})


class getStudent(View):

    model = Student

    def get(self, request, student_slug):
        student = self.model.objects.get(slug=student_slug)
        return render(request, 'student/student_detail.html', {'student': student})


class getStudents(View):

    model = Student

    def get(self, request):
        options, filter = pick(request.GET)
        resQuery =  self.model.objects.filter(**filter)

        if(options.get('order_by',None) != None):
            resQuery = resQuery.order_by(options['order_by'])

        students = resQuery[0:options['limit']]
        return render(request, 'student/student_list.html', {'students': students})


class deleteStudent(View):

    model = Student

    def get(self, request, student_slug):
        student = self.model.objects.get(slug=student_slug)
        return render(request, 'student/student_confirm_delete.html', {'student': student})

    
    def post(self, request, student_slug):
        student = get_object_or_404(self.model, slug=student_slug)
        student.delete()
        return redirect('student_student_list')


class updateStudent(View):

    model = Student
    form_class = StudentForm

    
    def get(self, request, student_slug):
        student = self.model.objects.get(slug=student_slug)
        studentForm = self.form_class(instance=student)
        return render(request, 'student/student_form_update.html', {'form': studentForm, 'student' : student})

    def post(self, request, student_slug):
        student = get_object_or_404(self.model, slug=student_slug)
        bound_form = self.form_class(request.POST, instance=student)
        if(bound_form.is_valid()):
            updated_student = bound_form.save()
            messages.success(request, "Update is succesfull")
            return redirect(updated_student)
        return render(request, 'student/student_form_update.html', {'form': bound_form, 'student' : student})








        
