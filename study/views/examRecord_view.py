from ..models import SubjectExamRecord

def addExamRecordInView(subject):
    return SubjectExamRecord.objects.create(subject=subject)

def updateExamRecordInView(subject, examMark):
    subjectRecord = SubjectExamRecord.object.get(subject=subject)
    subjectRecord.totalExam += 1
    subjectRecord.totalMarks += examMark 

def deleteExamRecordInView(subject, examMark):
    subjectRecord = SubjectExamRecord.object.get(subject=subject)
    subjectRecord.totalExam -= 1
    subjectRecord.totalMarks -= examMark 

def updateExamRecord(exam):
    subjectRecord = SubjectExamRecord.object.get(subject=exam.subject)
    subjectRecord.totalExam += 1
    subjectRecord.totalMarks += exam.marks 

def deleteExamRecord(exam):
    subjectRecord = SubjectExamRecord.object.get(subject=exam.subject)
    subjectRecord.totalExam -= 1
    subjectRecord.totalMarks -= exam.marks  