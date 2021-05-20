from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from resultMaker import settings

# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullName = models.CharField("Full Name", max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text="A label for URL config.")
    rollNumber = models.PositiveIntegerField("Roll Number", default = 1, validators=[MinValueValidator(1), MaxValueValidator(60)])
    std = models.PositiveIntegerField("Standard", default=11, validators=[MinValueValidator(11), MaxValueValidator(12)])
    DIVSION_CHOICES = [('A','A'), ('B','B'), ('C','C'), ('D','D')]
    div = models.CharField("Divison", max_length=1, choices=DIVSION_CHOICES, default='A')
    emailId = models.EmailField("Student Email Id", max_length=30, unique=True, null=True)
    parentEmailId = models.EmailField("Parent Email Id", max_length=30, unique=True)
    admissionYear = models.CharField("Admission Year", max_length=4)

    def __str__(self):
        return "Student : {}-{} R-{} {}".format(self.std, self.div, self.rollNumber, self.fullName)

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
        return "Student Profile : {}-{} R-{} {}".format(self.student.std, self.student.div, self.student.rollNumber, self.student.fullName)

    def get_absolute_url(self):
        return reverse('student_profile_get',kwargs={'profile_slug':self.slug})
    
    def get_update_url(self):
        return reverse('student_profile_update',kwargs={'profile_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('student_profile_delete',kwargs={'profile_slug':self.slug})

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Profile._meta.fields if field.verbose_name not in ['student']]



class ParentProfile(models.Model):
 
    slug = models.SlugField(max_length=50, unique=True, help_text="A label for URL config.")
    fatherName =  models.CharField('Father Name',max_length=40)
    motherName =  models.CharField('Mother Name',max_length=40)
    fatherBussiness =  models.CharField('Father Bussiness', max_length=30)
    motherBussiness = models.CharField('Mother Bussiness',max_length=30, null=True, blank=True)
    fatherStudy = models.CharField('Father Education', max_length=20, null=True, blank=True)
    motherStudy = models.CharField('Mother Education', max_length=20, null=True, blank=True)
    phoneNumber = models.CharField("Parent Phone Number",max_length=12, unique=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parent_profile')

    def __str__(self):
        # parent Profile : 11-A R-30 panseriya Aatman 
        return "parent Profile : {}-{} R-{} {}".format(self.student.std, self.student.div, self.student.rollNumber, self.student.fullName)

    def get_absolute_url(self):
        return reverse('student_parent_get',kwargs={'parent_profile_slug':self.slug})
    
    def get_update_url(self):
        return reverse('student_parent_update',kwargs={'parent_profile_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('student_parent_delete',kwargs={'parent_profile_slug':self.slug})
    
    def get_fields(self):
       return [(field.verbose_name, field.value_to_string(self)) for field in ParentProfile._meta.fields if field.verbose_name not in ['student']]





