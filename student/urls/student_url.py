from django.urls import path,include
from ..views import CreateStudent, GetStudent, GetStudents, DeleteStudent, UpdateStudent, GetExamResult
from . import studentProfile_url as studentProfileURL
from . import parentProfile_url  as parentProfileURL

urlpatterns = [
    path('profile/',include(studentProfileURL)),
    path('parent-profile/',include(parentProfileURL)),
    path('result/<slug:student_slug>/', GetExamResult.as_view(), name="student_exam_result"),
    path('delete/<slug:student_slug>/',DeleteStudent.as_view(), name="student_student_delete"),
    path('update/<slug:student_slug>/',UpdateStudent.as_view(), name="student_student_update"),
    path('create/',CreateStudent.as_view(),name="student_student_create"),
    path('list/',GetStudents.as_view(), name="student_student_list"),
    path('<slug:student_slug>/',GetStudent.as_view(), name="student_student_get"),

]