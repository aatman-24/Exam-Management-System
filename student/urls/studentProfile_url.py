from django.urls import path
from ..views import CreateStudentProfile, UpdateStudentProfile, GetStudentProfile, DeleteStudentProfile

urlpatterns = [
    path('create/<slug:student_slug>/', CreateStudentProfile.as_view(), name='student_profile_create'),
    path('update/<slug:profile_slug>/', UpdateStudentProfile.as_view(), name='student_profile_update'),
    path('delete/<slug:profile_slug>/', DeleteStudentProfile.as_view(), name='student_profile_delete'),
    path('<slug:profile_slug>/', GetStudentProfile.as_view(), name='student_profile_get'),
]

