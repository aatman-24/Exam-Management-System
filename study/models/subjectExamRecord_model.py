from django.db import models
from .subject_model import Subject
from django.shortcuts import reverse


class SubjectExamRecord(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="exam_record")
    totalMarks = models.IntegerField("Subject Total Marks", default=0)
    totalExam = models.IntegerField("Subject Total Exam", default=0)

    def __str__(self):
        return f"{self.subject}'s - Record"