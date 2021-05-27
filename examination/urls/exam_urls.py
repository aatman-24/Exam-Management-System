from django.urls import path
from ..views import CreateExam, GetExam, UpdateExam, DeleteExam, GetExams, GetExamResult

urlpatterns = [
    path('update/<slug:exam_slug>/', UpdateExam.as_view(), name='examination_exam_update'),
    path('delete/<slug:exam_slug>/', DeleteExam.as_view(), name='examination_exam_delete'),
    path('result/<slug:exam_slug>/', GetExamResult.as_view(), name='examination_exam_result'),
    path('create/', CreateExam.as_view(), name='examination_exam_create'),
    path('list/', GetExams.as_view(), name='examination_exam_list'),
    path('past_exams/', GetExams.as_view(exam_type="past"), name='examination_exam_pastExam'),
    path('future_exams/', GetExams.as_view(exam_type="future"), name='examination_exam_futureExam'),
    path('<slug:exam_slug>/', GetExam.as_view(), name='examination_exam_get'),
]
