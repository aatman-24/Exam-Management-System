from django.urls import path
from ..views import CreateParentProfile, UpdateParentProfile, GetParentProfile, DeleteParentProfile

urlpatterns = [
    path('update/<slug:parent_profile_slug>/', UpdateParentProfile.as_view(), name='student_parent_update'),
    path('delete/<slug:parent_profile_slug>/', DeleteParentProfile.as_view(), name='student_parent_delete'),
    path('create/<slug:student_slug>/',CreateParentProfile.as_view(), name='student_parent_create'),
    path('<slug:parent_profile_slug>/', GetParentProfile.as_view(), name='student_parent_get'),
]
