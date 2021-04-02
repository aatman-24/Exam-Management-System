from django.shortcuts import render
from django.views.generic import View
from django import http
from ..forms import ParentProfileForm
from ..models import ParentProfile, Student
from django.template.context_processors import csrf
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .student_view import getStudentBySlug


class createParentProfile(View):

    model = ParentProfile
    form_class = ParentProfileForm

    def get(self, request, student_slug):
        student = Student.objects.get(slug=student_slug)
        form = self.form_class()
        return render(request, 'student/parentProfile_form.html', {'form':form, 'student':student})
    
    def post(self, request, student_slug):
        student = Student.objects.get(slug=student_slug)
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newParentProfile = bound_form.save(commit=False)
            newParentProfile.student = student
            newParentProfile.save()
            return redirect(newParentProfile)
        else:
            return render(request, 'student/parentProfile_form.html', {'form':bound_form, 'student':student})


class getParentProfile(View):

    model = ParentProfile           

    def get(self, request, parent_profile_slug):
        parentProfile = self.model.objects.get(slug=parent_profile_slug)
        student = parentProfile.student
        return render(request, 'student/parentProfile_detail.html', {'parentProfile': parentProfile, 'student':student})



class deleteParentProfile(View):

    model = ParentProfile

    def get(self, request, parent_profile_slug):
        parentProfile = self.model.objects.get(slug=parent_profile_slug)
        return render(request, 'student/parentProfile_confirm_delete.html', {'parentProfile': parentProfile})

    
    def post(self, request, parent_profile_slug):
        parentProfile = get_object_or_404(self.model, slug=parent_profile_slug)
        parentProfile.delete()
        return redirect('student_profile_list')


class updateParentProfile(View):

    model = ParentProfile
    form_class = ParentProfileForm

    def get(self, request, parent_profile_slug):
        parentProfile = self.model.objects.get(slug=parent_profile_slug)
        parentForm = self.form_class(instance=parentProfile)
        return render(request, 'student/parentProfile_form_update.html', {'form': parentForm, 'parentProfile' : parentProfile})


    def post(self, request, parent_profile_slug):
        parentProfile = get_object_or_404(self.model, slug=parent_profile_slug)
        bound_form = self.form_class(request.POST, instance=parentProfile)
        if(bound_form.is_valid()):
            updated_profile = bound_form.save()
            messages.success(request, "Update is succesfull")
            return redirect(updated_profile)
        return render(request, 'student/parentProfile_form_update.html', {'form': bound_form, 'parentProfile' : parentProfile})









        
