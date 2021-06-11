import openpyxl
from student.models import Student
from examination.models import Exam
from .models import Result
from datetime import datetime

def getMark(sheet):
    
    marks = dict()
    absentNumber =  []
    max_row = sheet.max_row

    for i in range(2, max_row):
        if(sheet['B' + str(i)].value == 'AB'):
            absentNumber.append(sheet['A'+str(i)].value)
        elif(sheet['B' + str(i)].value == None):
            break
        else:
            marks[sheet['A'+str(i)].value] = sheet['B'+str(i)].value
            
    return marks, absentNumber


def generateRank(marks_dict, absentNumber):

    marks_dict = dict(sorted(marks_dict.items(), key = lambda x : x[1], reverse=True))
        
    rank = 0
    previousMark = -1
    ranked = dict()
    for rollnum, mark in marks_dict.items():
        
        if(mark == previousMark):
            ranked[rollnum] = rank
        else:
            rank += 1
            ranked[rollnum] = rank
            previousMark = mark

    rank += 1
    for rollnum in absentNumber:
         ranked[rollnum] = rank
            
    return ranked



def makeResult(fileName, sheetName='Sheet1'):
    wb = openpyxl.load_workbook(fileName)
    sheet =  wb[sheetName]

    exam = Exam.objects.get(examName = sheet['F1'].value)
    std = sheet['F3'].value
    div = sheet['F4'].value

    marks, absentNumber = getMark(sheet)
    ranked = generateRank(marks, absentNumber)

    for rollnum, mark in marks.items():

        student = Student.objects.get(rollNumber = rollnum, std = std, div = div)
        created_result = Result.objects.create(
            exam = exam,
            student = student,
            marks = mark,
            rank = ranked[rollnum],
            absent = (mark == 'AB'),
            slug = exam.slug + ' ' + student.slug
        )
        created_result.save()