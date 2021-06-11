from django.db import models
from .subject_model import Subject
from django.shortcuts import reverse
from django.utils.text import slugify
from autoslug import AutoSlugField

def mixSlugExamRecord(instance):
    return slugify(instance.subject) + "- exam-record"

class SubjectExamRecord(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="exam_record")
    totalMarks = models.IntegerField("Subject Total Marks", default=0)
    totalExam = models.IntegerField("Subject Total Exam", default=0)
    slug = AutoSlugField(populate_from=mixSlugExamRecord, unique=('subject'))

    def __str__(self):
        return f"{self.subject}'s - Record"