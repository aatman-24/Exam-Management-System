from django.urls import path
from ..views import UploadResultFile, GetResult, UpdateResult, DeleteResult, CreateResult

urlpatterns = [
    path('create/<slug:exam_slug>/<slug:student_slug>/', CreateResult.as_view(), name='result_result_create'),
    path('update/<slug:result_slug>/', UpdateResult.as_view(), name='result_result_update'),
    path('delete/<slug:result_slug>/', DeleteResult.as_view(), name='result_result_delete'),
    path('upload/<slug:exam_slug>/', UploadResultFile.as_view(), name='upload_result'),
    path('<slug:result_slug>/', GetResult.as_view(), name='result_result_get'),
]
