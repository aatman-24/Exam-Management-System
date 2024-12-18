from django.shortcuts import render
from django.views.generic import View
from django import http
from ..forms import StudentProfileForm
from ..models import Profile, Student
from ..utils import pick
from .student_view import getStudentBySlug
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

class createStudentProfile(View):

    model = Profile
    form_class = StudentProfileForm

    def get(self, request, student_slug):
        student = Student.objects.get(slug=student_slug)
        form = self.form_class()
        return render(request, 'student/studentProfile_form.html' , {'form':form, 'student': student})
    
    def post(self, request, student_slug):
        student = Student.objects.get(slug=student_slug)
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newStudentProfile = bound_form.save(commit=False)
            newStudentProfile.student = student
            newStudentProfile.save()
            return redirect(newStudentProfile)
        else:
           return render(request, 'student/studentProfile_form.html' , {'form':bound_form, 'student':student})

class getStudentProfile(View):

    model = Profile           

    def get(self, request, profile_slug):
        profile = self.model.objects.get(slug=profile_slug)
        student = profile.student
        return render(request, 'student/studentProfile_detail.html', {'profile': profile, 'student':student})


class deleteStudentProfile(View):

    model = Profile

    def get(self, request, profile_slug):
        profile = self.model.objects.get(slug=profile_slug)
        return render(request, 'student/studentProfile_confirm_delete.html', {'profile': profile})

    
    def post(self, request, profile_slug):
        profile = get_object_or_404(self.model, slug=profile_slug)
        profile.delete()
        return redirect('student_profile_list')


class updateStudentProfile(View):

    model = Profile
    form_class = StudentProfileForm

    def get(self, request, profile_slug):
        profile = self.model.objects.get(slug=profile_slug)
        profileForm = self.form_class(instance=profile)
        return render(request, 'student/studentProfile_form_update.html', {'form': profileForm, 'profile' : profile})


    def post(self, request, profile_slug):
        profile = get_object_or_404(self.model, slug=profile_slug)
        bound_form = self.form_class(request.POST, instance=profile)
        if(bound_form.is_valid()):
            updated_profile = bound_form.save()
            messages.success(request, "Update is succesfull")
            return redirect(updated_profile)
        return render(request, 'student/studentProfile_form_update.html', {'form': bound_form, 'profile' : profile})








        
