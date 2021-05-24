from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse
from config.subject import  SUBJECTS_CHOICES


class Subject(models.Model):

    subjectName = models.CharField("Subject Name",choices=SUBJECTS_CHOICES, max_length=20)
    standard = models.PositiveIntegerField("Standard", default=11, validators=[MinValueValidator(11), MaxValueValidator(12)], null=False, blank=False)
    totalMarks = models.IntegerField("Total Exam Marks", default=0)
    totalExam = models.IntegerField("Total Exam", default=0)
    currentYear = models.DateField(auto_now_add=True, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True, help_text="A label for URL config.")
    
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

    
class SubjectExamRecord(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="exam_record")
    totalMarks = models.IntegerField("Subject Total Marks", default=0)
    totalExam = models.IntegerField("Subject Total Exam", default=0)

    def __str__(self):
        return f"{self.subject}'s - Record"