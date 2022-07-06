from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import sqlalchemy as sal
from sqlalchemy import create_engine
from django.db import connections

def index(request):
    return HttpResponse('Главная страница Hermes')
    

def categories(request):
 
    cursor = connections['analytic'].cursor()
    filid_list = cursor.execute("SELECT UserLogin FROM AnalyticReports.payment.People WHERE UserID = 9")
        
        
    return HttpResponse(filid_list)
 