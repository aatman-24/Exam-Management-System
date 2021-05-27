from django.urls import path
from ..views import CreateSubject, GetSubject, GetSubjects, DeleteSubject, Updatesubject

urlpatterns = [
    path("update/<slug:subject_slug>/", Updatesubject.as_view(), name="study_subject_update"),
    path("delete/<slug:subject_slug>/", DeleteSubject.as_view(), name="study_subject_delete"),
    path("create/", CreateSubject.as_view(), name="study_subject_create"),
    path("current/", GetSubjects.as_view(), name="study_subject_curYearList"),
    path("list/", GetSubjects.as_view(this_year=False), name="study_subject_list"),
    path("<slug:subject_slug>/", GetSubject.as_view(), name="study_subject_get"),      
]


