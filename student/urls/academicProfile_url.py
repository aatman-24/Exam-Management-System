from django.urls import path
from ..views import CreateAcademicProfile, GetAcademicProfile

urlpatterns = [
    path('create/', CreateAcademicProfile.as_view(), name='student_academicprofile_create'),
    # path('update/<slug:profile_slug>/', UpdateStudentProfile.as_view(), name='student_profile_update'),
    # path('delete/<slug:profile_slug>/', DeleteStudentProfile.as_view(), name='student_profile_delete'),
    path('<slug:academic_slug>/', GetAcademicProfile.as_view(), name='student_academicprofile_get'),
]

