from django.urls import path, include
from . import subject_urls as SubjectURL

urlpatterns = [
    path('subject/', include(SubjectURL)),
]