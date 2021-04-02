from django.db import models
from config.subject import SUBJECTS
from django.shortcuts import reverse

class Exam(models.Model):

    SUBJECTS_CHOICES =[(name,name) for name in SUBJECTS]
    subject = models.CharField(verbose_name="Subject",choices= SUBJECTS_CHOICES, max_length=20)

    slug = models.SlugField(max_length=50, unique=True, help_text="A label for URL config.")
    syallbus = models.CharField(verbose_name="Syallbus", max_length=140)
    examDate = models.DateField(verbose_name="Exam Date", auto_now=False, auto_now_add=False, null=False, blank=False)
    marks = models.IntegerField("Total Marks")
    description = models.CharField("Description", max_length=50, null=True, blank=True)
    examName = models.CharField("Exam Name", max_length=20)
    resultPublished = models.BooleanField("Result Published", default=False)

    def __str__(self):
        return self.examName 

    class Meta:
        ordering = ['-examDate']

    def get_absolute_url(self):
        return reverse('examination_exam_get',kwargs={'exam_slug':self.slug})
    
    def get_update_url(self):
        return reverse('examination_exam_update',kwargs={'exam_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('examination_exam_delete',kwargs={'exam_slug':self.slug})

    def get_fields(self):
        all_fields = [(field.verbose_name, field.value_to_string(self)) for field in Exam._meta.fields]
        return all_fields
