from ..models import AcademicProfile, SubjectMarks
from study.models import Subject

def initialize_subject_for_student(studentAcademic, subject):
        
    subjectmark = SubjectMarks.objects.create(student=studentAcademic.student, subject=subject)
    subjectmark.save()
    
    studentAcademic.subjectmarks.add(subjectmark)
    studentAcademic.save()
    
def add_student_subject_marks(student, subject, totalMarks):    
    submark = SubjectMarks.objects.get(student=student, subject=subject)
    submark.totalMarks += totalMarks
    submark.totalExam  += 1
    submark.save()
    
    academicProfile = submark.academic.get()
    academicProfile.totalExam += 1
    academicProfile.totalMarks += totalMarks
    academicProfile.save()
    
    

def update_student_subject_marks(student, subject, update_marks):
    submark = SubjectMarks.objects.get(student=student, subject=subject)
    submark.totalMarks += update_marks
    submark.save()
