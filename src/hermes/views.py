from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# import sqlalchemy as sal
# from sqlalchemy import create_engine
# import pyodbc

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
    
    
    # return HttpResponse(filid_list)
    return HttpResponse('Категории')