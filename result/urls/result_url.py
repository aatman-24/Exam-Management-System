from django.urls import path
from ..views import UploadResultFile, GetResult, UpdateResult, DeleteResult, CreateResult, GetResults, DownloadResultFile, DownloadResultFile

urlpatterns = [
    path('create/<slug:exam_slug>/<slug:student_slug>/', CreateResult.as_view(), name='result_result_create'),
    path('update/<slug:result_slug>/', UpdateResult.as_view(), name='result_result_update'),
    path('delete/<slug:result_slug>/', DeleteResult.as_view(), name='result_result_delete'),
    path('download/file/<slug:exam_slug>/', DownloadResultFile.as_view(), name='result_file_download'),
    path('upload/<slug:exam_slug>/', UploadResultFile.as_view(), name='upload_result'),
    path('list/', GetResults.as_view(), name='result_result_list'),
    path('<slug:result_slug>/', GetResult.as_view(), name='result_result_get'),
]
