from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth import get_user
    
from ..models import AcademicProfile, SubjectMarks
from .subjectMarks_view import initialize_subject_for_student
from study.models import Subject
from datetime import datetime

def add_subjects_for_student(studentAcademic, standard):
    
    subjects = Subject.objects.filter(standard = standard, currentYear__year = datetime.now().year)
    for subject in subjects:
        initialize_subject_for_student(studentAcademic, subject)

def get_student_from_request(request):
    user = get_user(request)
    if(user is not None):
        pass
    return user.student 

class CreateAcademicProfile(View):
    
    def get(self, request):
        student = get_student_from_request(request) 
        standard = student.std
                     
        academic = AcademicProfile.objects.create(student = student)
        academic.save()
        
        add_subjects_for_student(academic, standard)
    
        return HttpResponse("Success")
        
        
class GetAcademicProfile(View):

    model = AcademicProfile

    def get(self, request):
        student = get_student_from_request(request)
        academicprofile = student.academicprofile
        subjectMarks = academicprofile.subjectmarks.all()

        context = {
            'academicprofile': academicprofile,
            'subjecmarks' : subjectMarks,  
        }
                
        return render(request, 'student/student_detail.html', context)       
    
    