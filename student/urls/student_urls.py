from django.urls import path,include
from ..views.student_view import studentCreate, getStudent, getStudents, deleteStudent, updateStudent
from ..urls import studentProfile_urls as studentProfileURL
from ..urls import parentProfile_urls as parentProfileURL

urlpatterns = [
    path('profile/',include(studentProfileURL)),
    path('parent-profile/',include(parentProfileURL)),
    path('<slug:student_slug>/delete/',deleteStudent.as_view(), name="student_student_delete"),
    path('<slug:student_slug>/update/',updateStudent.as_view(), name="student_student_update"),
    path('create/',studentCreate.as_view(),name="student_student_create"),
    path('list/',getStudents.as_view(), name="student_student_list"),
    path('<slug:student_slug>/',getStudent.as_view(), name="student_student_get"),
]

# student/profile/aatman-panseriya/create/