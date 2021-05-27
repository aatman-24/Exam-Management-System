from django.db import models
from student.models import Student
from examination.models import Exam
from django.shortcuts import reverse


# Create your models here.

class Result(models.Model):

    student = models.ForeignKey(Student, verbose_name=("result"),related_name = "result", on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,related_name="result", on_delete=models.CASCADE)
    marks = models.CharField(verbose_name="Marks", max_length=4)
    rank = models.PositiveIntegerField(verbose_name="Rank", default=0)
    publishedDate = models.DateTimeField(verbose_name="Result Published Date", auto_now = True)
    slug = models.SlugField(max_length=50, unique=True, help_text="A label for URL config.")
    absent = models.BooleanField(verbose_name="Absent", default=False)
    
    
    def __str__(self):
        return self.exam.examName + "'s" + self.student.fullName

    class Meta:
        ordering = ['-publishedDate']

    def get_absolute_url(self):
        return reverse('result_result_get',kwargs={'result_slug':self.slug})
    
    def get_update_url(self):
        return reverse('result_result_update',kwargs={'result_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('result_result_delete',kwargs={'result_slug':self.slug})

    def get_fields(self):
        all_fields = [(field.verbose_name, field.value_to_string(self)) for field in Result._meta.fields]
        return all_fields


