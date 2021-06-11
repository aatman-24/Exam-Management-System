from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from organizer import settings
from autoslug import AutoSlugField

class Student(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullName = models.CharField("Full Name", max_length=50)
    rollNumber = models.PositiveIntegerField("Roll Number", default = 1, validators=[MinValueValidator(1), MaxValueValidator(60)])
    std = models.PositiveIntegerField("Standard", default=11, validators=[MinValueValidator(11), MaxValueValidator(12)])
    DIVSION_CHOICES = [('A','A'), ('B','B'), ('C','C'), ('D','D')]
    div = models.CharField("Divison", max_length=1, choices=DIVSION_CHOICES, default='A')
    emailId = models.EmailField("Student Email Id", max_length=30, unique=True, null=True)
    parentEmailId = models.EmailField("Parent Email Id", max_length=30, unique=True)
    admissionYear = models.CharField("Admission Year", max_length=4)
    slug = AutoSlugField(populate_from='fullName', unique=True)
    

    def __str__(self):
        return "{}".format(self.fullName)

    class Meta:
        verbose_name = 'Student'
        ordering = ['rollNumber']
        unique_together = ("rollNumber", "std", "div")

    def get_absolute_url(self):
        return reverse('student_student_get',kwargs={'student_slug':self.slug})
    
    def get_update_url(self):
        return reverse('student_student_update',kwargs={'student_slug':self.slug})

    def get_result_url(self):
        return reverse('student_exam_result', kwargs={'student_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('student_student_delete',kwargs={'student_slug':self.slug})

    def get_fields(self):
        all_fields = [(field.verbose_name, field.value_to_string(self)) for field in Student._meta.fields]
        return all_fields