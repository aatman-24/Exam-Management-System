from django.db import models
from django.shortcuts import reverse
from .student_model import Student
from study.models import Subject


class SubjectMarks(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    totalMarks = models.IntegerField("Total Marks", default=0)
    totalExam = models.IntegerField("Total Exam", default=0)

    class Meta:
        ordering = ['student', 'subject']

    def __str__(self):
        return f"{self.student} - {self.subject.subjectName}"

class AcademicProfile(models.Model):

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    totalMarks = models.IntegerField("Total Marks", default=0)
    totalExam = models.IntegerField("Total Exam", default=0)
    subjectmarks = models.ManyToManyField(SubjectMarks, related_name='academic')

    class Meta:
        ordering = ['student']

    def __str__(self):
        return f"{self.student} - {self.totalMarks}"
