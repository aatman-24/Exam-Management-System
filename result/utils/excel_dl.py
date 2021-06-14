from django.shortcuts import render
from django.http.response import HttpResponse
from xlsxwriter.workbook import Workbook
from ..utils import *
from .excel_design import *
from config.excel import *


def add_exam_subdetails(wb, ws, exam):
    
    # locked = wb.add_format({'locked': True})
    
    exam_sub_details_cell = wb.add_format(exam_sub_details)
    exam_sub_details_ans_cell = wb.add_format(exam_sub_details_ans)
    absent_cell = wb.add_format(absent)
    AB_cell = wb.add_format(AB)

    exam_date = exam.get_exam_date()
    exam_details = {
        'Exam ID' : exam.id,
        'Exam Name' : exam.examName,
        'Exam Date' : exam_date.strftime("%d %b %Y"),
        'Standard' : exam.standard,
        'Subject': exam.subject.subjectName,
        'Total Marks' : exam.marks,
        'Slug' : exam.slug
    }

    start_row = DETAILS_START_ROW
    col = DETAILS_START_COL
      
    for row_num, exam_header in enumerate(exam_details.keys()):
        ws.write(row_num+start_row, col, exam_header, exam_sub_details_cell)
        ws.write(row_num+start_row, col+1, exam_details[exam_header], exam_sub_details_ans_cell)
    
    #Added Absent Cell    
    ws.write(len(exam_details) + start_row + 2, col, "Absent", absent_cell)
    ws.write(len(exam_details) + start_row + 2, col+1, "ABS", AB_cell)


def add_exam_details(wb, ws, exam):
    
    do_not_modify_cell = wb.add_format(do_not_modify)
    exam_details_cell = wb.add_format(exam_detail)

    modify_width = len("Do not modify this Details")
    ws.merge_range(D0_NOT_MODIFY_CELL, "Do not modify this Details", do_not_modify_cell)
    ws.set_column(D0_NOT_MODIFY_START_COL, D0_NOT_MODIFY_START_COL+1, modify_width)
    ws.merge_range(DETAILS_TITLE, "Exam Details", exam_details_cell)
    
    add_exam_subdetails(wb, ws, exam)


def add_mark_data(wb, ws, Student):
    
    roll_number_cell = wb.add_format(roll_number_format)
    mark_cell = wb.add_format(marks)

    col = ROLL_NUMBER_START_COL
    row = ROLL_NUMBER_START_ROW
    
    student_roll_number = Student.objects.values_list('rollNumber', flat=True).all()

    for i, roll_number in enumerate(student_roll_number):
        ws.write(row+i, col, roll_number, roll_number_cell)
        ws.write(row+i, col+1, None, mark_cell)


def add_header(wb, ws):
    
    roll_number_header_cell = wb.add_format(roll_number_header)
    mark_header_cell = wb.add_format(mark_header)
    
    Header = ['Roll Number', 'Mark']
    Header_format = [roll_number_header_cell, mark_header_cell]
    
    row = ROLL_NUMBER_HEADER_ROW
    for col_num, header in enumerate(Header):
        ws.write(row, col_num, header, Header_format[col_num])
        
    width = len('Roll Number') + 5
    ws.set_column(0,1, width)


def add_data_to_worksheet(wb, ws, exam, Student):
        
    # Turn worksheet protection on.
    ws.protect()
    
    #Add Header
    add_header(wb,ws)
    
    #Add Data
    add_mark_data(wb,ws, Student)
    
    #Add Exam Details
    add_exam_details(wb,ws, exam)
    


    
    
    
    