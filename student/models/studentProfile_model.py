from django.db import models
from django.shortcuts import reverse
from .student_model import Student

class Profile(models.Model):
    birthDate = models.DateField('Birth Date')
    slug = models.SlugField(max_length=50, unique=True, help_text="A label for URL config.")
    GENDER_CHOICES = [('M','Male'), ('F','Female'), ('O','Other')]
    gender = models.CharField('Gender',choices=GENDER_CHOICES, default='M', max_length=1)
    phoneNumber = models.CharField("Phone Number",max_length=12, unique=True)
    previousSchool = models.CharField('Previous School', max_length=50, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='profile')
    
    def __str__(self):
        # Student Profile : 11-A R-30 panseriya Aatman 
        return "{} Profile".format(self.student)

    def get_absolute_url(self):
        return reverse('student_profile_get',kwargs={'profile_slug':self.slug})
    
    def get_update_url(self):
        return reverse('student_profile_update',kwargs={'profile_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('student_profile_delete',kwargs={'profile_slug':self.slug})

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Profile._meta.fields if field.verbose_name not in ['student']]

