from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse
from config.subject import  SUBJECTS_CHOICES
from autoslug import AutoSlugField
from django.utils.text import slugify

def mixSlugSubject(instance):
    return slugify(instance.subjectName) + "-std-" +  slugify(instance.standard)
    
class Subject(models.Model):

    subjectName = models.CharField("Subject Name",choices=SUBJECTS_CHOICES, max_length=20)
    standard = models.PositiveIntegerField("Standard", default=11, validators=[MinValueValidator(11), MaxValueValidator(12)], null=False, blank=False)
    totalMarks = models.IntegerField("Total Exam Marks", default=0)
    totalExam = models.IntegerField("Total Exam", default=0)
    currentYear = models.DateField(auto_now_add=True, null=False, blank=False)
    slug = AutoSlugField(populate_from=mixSlugSubject, unique_with=('subjectName','currentYear__year'))
    
    class Meta:
        unique_together = ("currentYear", "subjectName", "standard")

    def __str__(self):
        return f"{self.id} - {self.subjectName}"
        
    def get_absolute_url(self):
        return reverse('study_subject_get',kwargs={'subject_slug':self.slug})
    
    def get_update_url(self):
        return reverse('study_subject_update',kwargs={'subject_slug':self.slug})

    # def get_result_url(self):
    #     return reverse('student_exam_result', kwargs={'subject_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('study_subject_delete',kwargs={'subject_slug':self.slug})

    