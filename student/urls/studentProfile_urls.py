from django.urls import path
from ..views.studentProfile_view import createStudentProfile, updateStudentProfile, getStudentProfile, deleteStudentProfile

urlpatterns = [
    path('<slug:student_slug>/create/', createStudentProfile.as_view(), name='student_profile_create'),
    path('<slug:profile_slug>/update/', updateStudentProfile.as_view(), name='student_profile_update'),
    path('<slug:profile_slug>/delete/', deleteStudentProfile.as_view(), name='student_profile_delete'),
    path('<slug:profile_slug>/', getStudentProfile.as_view(), name='student_profile_get'),
]

