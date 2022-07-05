from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import sqlalchemy as sal
from sqlalchemy import create_engine
import pymssql
import pyodbc


def index(request):
    return HttpResponse('Главная страница Hermes')
    

def categories(request):
    # connection_string = 'mssql+pyodbc://KVCEN15-SQLS005.officekiev.fozzy.lan\\heavy005/SILPOAnalitic?driver=ODBC Driver 17 for SQL Server&charset=utf8&trusted_connection=yes&autocommit=true'
    # engine = sal.create_engine(connection_string)

    # SQL = "SELECT TOP 5 Filid from SILPOAnalitic.dbo.aid_filialsall"

    # print(f'request  string: {SQL}')
    # print()

    # with engine.connect() as connection:
    #     result = connection.execute(SQL)
    #     filid_list = []
    #     for row in result:
    #         filid_list.append(row)
            
    
    ################################
    
    # server = 'S-KV-CENTER-S59.officekiev.fozzy.lan' 
    # database = 'AnalyticReports' 
    # username = 'j-PaymentDev' 
    # password = 'V41m9i1Z90XPpdfaPICy' 
    # cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    # cursor = cnxn.cursor()
    
    # cursor.execute('SELECT UserLogin FROM AnalyticReports.payment.People WHERE UserID = 9')
    # filid_list = []
    # for row in cursor:
    #     filid_list.append(row)
    
    # conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
    #                     'Server=KVCEN15-SQLS005.officekiev.fozzy.lan\\heavy005;'
    #                     'Database=SILPOAnalitic;'
    #                     'Trusted_Connection=yes;')

    # SQL = "SELECT TOP 5 Filid from SILPOAnalitic.dbo.aid_filialsall"

    # print(f'request  string: {SQL}')
    # print()


    # result = conn.execute(SQL)
    # filid_list = []
    # for row in result:
    #     filid_list.append(row)
        
    # print(filid_list)
    
    from django.db import connections
    cursor = connections['analytic'].cursor()
    filid_list = cursor.execute("SELECT UserLogin FROM AnalyticReports.payment.People WHERE UserID = 9")
    # print(a)

    # filid_list = 0
        
        
    return HttpResponse(filid_list)
   
# from django.db import connections
# cursor = connections['analytic'].cursor()
# a = cursor.execute("SELECT UserLogin FROM AnalyticReports.payment.People WHERE UserID = 9")
# print(a)


# server = 'S-KV-CENTER-S59.officekiev.fozzy.lan'
# user = 'j-PaymentDev'
# password = 'V41m9i1Z90XPpdfaPICy'

# conn = pymssql.connect(server, user, password)
# cursor = conn.cursor()
# cursor.execute('SELECT UserLogin FROM AnalyticReports.payment.People WHERE UserID = 9')

# list = []
# for row in cursor:
#     list.append(row)

# print(list)

# conn.close()


# connection_string = 'mssql+pyodbc://KVCEN15-SQLS005.officekiev.fozzy.lan\\heavy005/SILPOAnalitic?driver=ODBC Driver 17 for SQL Server&charset=utf8&trusted_connection=yes&autocommit=true'
# engine = sal.create_engine(connection_string)

# SQL = "SELECT TOP 5 Filid from SILPOAnalitic.dbo.aid_filialsall"

# print(f'request  string: {SQL}')
# print()

# with engine.connect() as connection:
#     result = connection.execute(SQL)
#     filid_list = []
#     for row in result:
#         filid_list.append(row)
        
#     print(filid_list)


# conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
#                     'Server=KVCEN15-SQLS005.officekiev.fozzy.lan\\heavy005;'
#                     'Database=SILPOAnalitic;'
#                     'Trusted_Connection=yes;')

# SQL = "SELECT TOP 5 Filid from SILPOAnalitic.dbo.aid_filialsall"

# print(f'request  string: {SQL}')
# print()


# result = conn.execute(SQL)
# filid_list = []
# for row in result:
#     filid_list.append(row)
    
# print(filid_list)