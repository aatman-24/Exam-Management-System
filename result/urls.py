from django.urls import path
from .views import UploadResultFile, GetResult, UpdateResult, DeleteResult, CreateResult

urlpatterns = [
    path('<slug:exam_slug>/upload/', UploadResultFile.as_view(), name='upload_result'),
    path('<slug:result_slug>/', GetResult.as_view(), name='result_result_get'),
    path('<slug:result_slug>/update/', UpdateResult.as_view(), name='result_result_update'),
    path('<slug:result_slug>/delete/', DeleteResult.as_view(), name='result_result_delete'),
    path('<slug:exam_slug>/<slug:student_slug>/create/', CreateResult.as_view(), name='result_result_create'),
]
