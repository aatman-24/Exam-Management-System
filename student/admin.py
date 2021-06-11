from django.contrib import admin
from .models import Student, ParentProfile, Profile, AcademicProfile, SubjectMarks

# Register your models here.

admin.site.register(Student)
admin.site.register(ParentProfile)
admin.site.register(Profile)
admin.site.register(AcademicProfile)
admin.site.register(SubjectMarks)