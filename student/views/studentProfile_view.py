from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django import http
from django.contrib import messages

from ..forms import StudentProfileForm
from ..models import Profile, Student
from ..utils import pick
from .student_view import getStudentBySlug, verifyStudent
from users.decorator import class_login_required, class_require_authenticated_permisssion
from django.contrib.auth import get_user

@class_login_required
class CreateStudentProfile(View):

    model = Profile
    form_class = StudentProfileForm

    def get(self, request, student_slug):
        student = get_object_or_404(Student, slug = student_slug)
        verifyStudent(request, student)
        form = self.form_class()
        return render(request, 'student/studentProfile_form.html' , {'form':form, 'student': student})
    
    def post(self, request, student_slug):
        student = get_object_or_404(Student, slug = student_slug)
        verifyStudent(request, student)
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newStudentProfile = bound_form.save(commit=False)
            newStudentProfile.student = student
            newStudentProfile.save()
            return redirect(newStudentProfile)
        else:
           return render(request, 'student/studentProfile_form.html' , {'form':bound_form, 'student':student})

@class_login_required
class GetStudentProfile(View):

    model = Profile           

    def get(self, request, profile_slug):
        profile= get_object_or_404(self.model, slug = profile_slug)
        student = profile.student
        verifyStudent(request, student)
        return render(request, 'student/studentProfile_detail.html', {'profile': profile, 'student':student})

@class_require_authenticated_permisssion('student.manage_student')
class DeleteStudentProfile(View):

    model = Profile

    def get(self, request, profile_slug):
        profile= get_object_or_404(self.model, slug = profile_slug)
        return render(request, 'student/studentProfile_confirm_delete.html', {'profile': profile})

    
    def post(self, request, profile_slug):
        profile = get_object_or_404(self.model, slug=profile_slug)
        profile.delete()
        return redirect('student_profile_list')

@class_login_required
class UpdateStudentProfile(View):

    model = Profile
    form_class = StudentProfileForm

    def get(self, request, profile_slug):
        profile = get_object_or_404(self.model, slug = profile_slug)
        student = profile.student
        verifyStudent(request, student)
        profileForm = self.form_class(instance=profile)
        return render(request, 'student/studentProfile_form_update.html', {'form': profileForm, 'profile' : profile})


    def post(self, request, profile_slug):
        profile = get_object_or_404(self.model, slug=profile_slug)
        student = profile.student
        verifyStudent(request, student)
        bound_form = self.form_class(request.POST, instance=profile)
        if(bound_form.is_valid()):            
            updated_profile = bound_form.save()
            messages.success(request, "Update is succesfull")
            return redirect(updated_profile)
        return render(request, 'student/studentProfile_form_update.html', {'form': bound_form, 'profile' : profile})