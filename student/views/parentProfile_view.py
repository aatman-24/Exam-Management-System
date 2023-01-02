from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django import http
from django.contrib import messages
from django.core.exceptions import PermissionDenied


from .student_view import getStudentBySlug, verifyStudent
from ..forms import ParentProfileForm
from ..models import ParentProfile, Student
from users.decorator import class_login_required, class_require_authenticated_permisssion


@class_login_required
class CreateParentProfile(View):

    model = Student
    form_class = ParentProfileForm

    def get(self, request, student_slug):
        student = get_object_or_404(self.model, slug = student_slug)
        verifyStudent(request, student)
        form = self.form_class()
        return render(request, 'student/parentProfile_form.html', {'form':form, 'student':student})
    
    def post(self, request, student_slug):
        student= get_object_or_404(self.model, slug = student_slug)
        verifyStudent(request, student)
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            newParentProfile = bound_form.save(commit=False)
            newParentProfile.student = student
            newParentProfile.save()
            return redirect(newParentProfile)
        else:
            return render(request, 'student/parentProfile_form.html', {'form':bound_form, 'student':student})

@class_login_required
class GetParentProfile(View):

    model = ParentProfile           

    def get(self, request, parent_profile_slug):
        parentProfile = get_object_or_404(self.model, slug = parent_profile_slug)
        student = parentProfile.student
        verifyStudent(request, student)
        return render(request, 'student/parentProfile_detail.html', {'parentProfile': parentProfile, 'student':student})


@class_require_authenticated_permisssion('student.manage_student')
class DeleteParentProfile(View):

    model = ParentProfile

    def get(self, request, parent_profile_slug):
        parentProfile = get_object_or_404(self.model, slug = parent_profile_slug)
        return render(request, 'student/parentProfile_confirm_delete.html', {'parentProfile': parentProfile})

    
    def post(self, request, parent_profile_slug):
        parentProfile = get_object_or_404(self.model, slug=parent_profile_slug)
        parentProfile.delete()
        return redirect('student_profile_list')

@class_login_required
class UpdateParentProfile(View):

    model = ParentProfile
    form_class = ParentProfileForm

    def get(self, request, parent_profile_slug):
        parentProfile = get_object_or_404(self.model, slug = parent_profile_slug)
        student = parentProfile.student
        verifyStudent(request, student)
        parentForm = self.form_class(instance=parentProfile)
        return render(request, 'student/parentProfile_form_update.html', {'form': parentForm, 'parentProfile' : parentProfile})


    def post(self, request, parent_profile_slug):
        parentProfile = get_object_or_404(self.model, slug=parent_profile_slug)
        student = parentProfile.student
        verifyStudent(request, student)
        bound_form = self.form_class(request.POST, instance=parentProfile)
        if(bound_form.is_valid()):
            updated_profile = bound_form.save()
            messages.success(request, "Update is succesfull")
            return redirect(updated_profile)
        return render(request, 'student/parentProfile_form_update.html', {'form': bound_form, 'parentProfile' : parentProfile})









        
