from django.urls import path
from ..views.subject_views import createSubject, getSubject, getSubjects, deleteSubject, updatesubject

urlpatterns = [
    path("<slug:subject_slug>/update/", updatesubject.as_view(), name="study_subject_update"),
    path("<slug:subject_slug>/delete/", deleteSubject.as_view(), name="study_subject_delete"),
    path("create/", createSubject.as_view(), name="study_subject_create"),
    path("current/", getSubjects.as_view(), name="study_subject_curYearList"),
    path("list/", getSubjects.as_view(this_year=False), name="study_subject_list"),
    path("<slug:subject_slug>/", getSubject.as_view(), name="study_subject_get"),   
]


