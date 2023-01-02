from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth import get_user,get_user_model
from datetime import datetime
    
from ..models import AcademicProfile, SubjectMarks
from .subjectMarks_view import initialize_subject_for_student
from study.models import Subject
from users.decorator import class_login_required
from .student_view import getStudentBySlug, verifyStudent

def add_subjects_for_student(studentAcademic, standard):
    
    subjects = get_list_or_404(Subject, standard = standard, currentYear__year = datetime.now().year)
    for subject in subjects:
        initialize_subject_for_student(studentAcademic, subject)

def get_student_from_request(request):
    user = get_user(request)
    User = get_user_model()
    if(user is None):
        raise User.DoesNotExist("User Not Found")
    return user.student 

@class_login_required
class CreateAcademicProfile(View):
    
    def get(self, request):
        student = get_student_from_request(request) 
        standard = student.std
                     
        academic = AcademicProfile.objects.create(student = student)
        academic.save()
        
        add_subjects_for_student(academic, standard)
    
        return HttpResponse("Success")
        
@class_login_required  
class GetAcademicProfile(View):

    model = AcademicProfile

    def get(self, request, academic_slug):
        
        academicprofile = get_object_or_404(self.model, slug=academic_slug)
        verifyStudent(request, academicprofile.student)
        subjectMarks = academicprofile.subjectmarks.all()
        context = {
            'academicprofile': academicprofile,
            'subjecmarks' : subjectMarks,  
        }
        return render(request, 'student/student_detail.html', context)       
    
    
def getTopScorer(std, top=None): 
    topStudents = AcademicProfile.objects.filter(student__std = std).order_by('-totalMarks', 'totalExam')
    numOfStudent = len(topStudents)
    print(numOfStudent)
    if(top is None):
        top = numOfStudent
    return topStudents[: min(numOfStudent, top)]