from django.urls import path
from ..views import createExam , getExam, updateExam, deleteExam, getExams

urlpatterns = [
    path('<slug:exam_slug>', getExam.as_view(), name='examination_exam_get'),
    path('create/', createExam.as_view(), name='examination_exam_create'),
    path('list/', getExams.as_view(), name='examination_exam_list'),
    path('pasts/', getExams.as_view(exam_type="past"), name='examination_exam_pastExam'),
    path('futures/', getExams.as_view(exam_type="future"), name='examination_exam_futureExam'),
    path('<slug:exam_slug>/update', updateExam.as_view(), name='examination_exam_update'),
    path('<slug:exam_slug>/delete', deleteExam.as_view(), name='examination_exam_delete'),
]
