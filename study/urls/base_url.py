from django.urls import path, include
from . import subject_url as SubjectURL

urlpatterns = [
    path('subject/', include(SubjectURL)),
]