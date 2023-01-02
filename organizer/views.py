from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django import http
from django.contrib import messages
from django.contrib.auth import get_user
from django.core.exceptions import PermissionDenied
from users.decorator import class_login_required, class_require_authenticated_permisssion

from examination.views import getExams
from student.views import getTopScorer


class HomeView(View):
    
    def get(self, request):
        
        topScorerOf11 = getTopScorer('11', 3)
        topScorerOf12 = getTopScorer('12', 3)
        
        futureExams11 = getExams("future", 11, 3)
        futureExams12 = getExams("future", 12, 3)
        
        pastExams11 = getExams("past", 11, 3)
        pastExams12 = getExams("past", 12, 3)
        
        
        context = {
            'topScorerOf11' : topScorerOf11,
            'topScorerOf12' : topScorerOf12,
            'futureExams11' : futureExams11,
            'futureExams12' : futureExams12,
            'pastExams11' : pastExams11,
            'pastExams12' : pastExams12,
        }
        
        return render(request, 'home.html', context)
        
        
        
        
    
    
    