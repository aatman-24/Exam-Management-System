from django.db import models
from django.shortcuts import reverse
from .student_model import Student
from autoslug import AutoSlugField
from django.utils.text import slugify

def mixSlugParentProfile(instance):
    return slugify(instance.student) + "- parent-profile"

class ParentProfile(models.Model):

    fatherName =  models.CharField('Father Name',max_length=40)
    motherName =  models.CharField('Mother Name',max_length=40)
    fatherBussiness =  models.CharField('Father Bussiness', max_length=30)
    motherBussiness = models.CharField('Mother Bussiness',max_length=30, null=True, blank=True)
    fatherStudy = models.CharField('Father Education', max_length=20, null=True, blank=True)
    motherStudy = models.CharField('Mother Education', max_length=20, null=True, blank=True)
    phoneNumber = models.CharField("Parent Phone Number",max_length=12, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parent_profile')
    
    slug = AutoSlugField(populate_from=mixSlugParentProfile, unique_with=('student',))

    

    def __str__(self):
        # parent Profile : 11-A R-30 panseriya Aatman 
        return "{} Parent-profile".format(self.student)

    def get_absolute_url(self):
        return reverse('student_parent_get',kwargs={'parent_profile_slug':self.slug})
    
    def get_update_url(self):
        return reverse('student_parent_update',kwargs={'parent_profile_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('student_parent_delete',kwargs={'parent_profile_slug':self.slug})
    
    def get_fields(self):
       return [(field.verbose_name, field.value_to_string(self)) for field in ParentProfile._meta.fields if field.verbose_name not in ['student']]
