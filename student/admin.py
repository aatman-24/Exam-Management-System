from django.contrib import admin
from .models import Student, ParentProfile, Profile

# Register your models here.

admin.site.register(Student)
admin.site.register(ParentProfile)
admin.site.register(Profile)