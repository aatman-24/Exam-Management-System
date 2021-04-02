from django.urls import path
from ..views.parentProfile_view import createParentProfile, updateParentProfile, getParentProfile, deleteParentProfile

urlpatterns = [
    path('<slug:parent_profile_slug>/update/', updateParentProfile.as_view(), name='student_parent_update'),
    path('<slug:parent_profile_slug>/delete/', deleteParentProfile.as_view(), name='student_parent_delete'),
    path('<slug:parent_profile_slug>/', getParentProfile.as_view(), name='student_parent_get'),
    path('<slug:student_slug>/create/',createParentProfile.as_view(), name='student_parent_create'),
]
