from django.shortcuts import get_object_or_404
from ..models import SubjectExamRecord

def addExamRecordInView(subject):
    return SubjectExamRecord.objects.create(subject=subject)

def updateExamRecordInView(subject, examMark):
    subjectRecord = get_object_or_404(SubjectExamRecord, subject=subject)
    subjectRecord.totalExam += 1
    subjectRecord.totalMarks += examMark 

def deleteExamRecordInView(subject, examMark):
    subjectRecord = get_object_or_404(SubjectExamRecord, subject=subject)
    subjectRecord.totalExam -= 1
    subjectRecord.totalMarks -= examMark 

def updateExamRecord(exam):
    subjectRecord = get_object_or_404(SubjectExamRecord, subject=exam.subject)
    subjectRecord.totalExam += 1
    subjectRecord.totalMarks += exam.marks 

def deleteExamRecord(exam):
    subjectRecord = get_object_or_404(SubjectExamRecord, subject=exam.subject)
    subjectRecord.totalExam -= 1
    subjectRecord.totalMarks -= exam.marks  