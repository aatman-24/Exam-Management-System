from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from study.models import Subject
from autoslug import AutoSlugField
from django.utils.text import slugify


# def mixSlug(instance):
#     return slugify(instance.examName) + '-' + slugify(instance.subject) 
class Exam(models.Model):

    examName = models.CharField("Exam Name", max_length=20)
    examDate = models.DateField(verbose_name="Exam Date", auto_now=False, auto_now_add=False, null=False, blank=False)
    standard = models.PositiveIntegerField("Standard", default=11, validators=[MinValueValidator(11), MaxValueValidator(12)])
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    syallbus = models.CharField(verbose_name="Syallbus", max_length=250)
    marks = models.IntegerField(verbose_name="Total Marks")
    description = models.CharField("Description", max_length=50, null=True, blank=True)
    resultPublished = models.BooleanField("Result Published", default=False)
    slug = AutoSlugField(populate_from="examName", unique=True)

    def __str__(self):
        return self.examName 
        
    class Meta:
        ordering = ['-examDate']
        permissions = (("publish_exam","Can publish new Exams"),)

    def get_absolute_url(self):
        return reverse('examination_exam_get',kwargs={'exam_slug':self.slug})
    
    def get_update_url(self):
        return reverse('examination_exam_update',kwargs={'exam_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('examination_exam_delete',kwargs={'exam_slug':self.slug})
    
    def get_exam_date(self):
        return self.examDate
    
    def get_result_url(self):
        return reverse('examination_exam_result', kwargs={'exam_slug':self.slug})

    def get_fields(self):
        all_fields = [(field.verbose_name, field.value_to_string(self)) for field in Exam._meta.fields]
        return all_fields
