from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import mysql.connector 
from dbConnection.dbConnectionClass import DbConnector

# Create your views here.
def aapHome(request):
    connector=DbConnector()
    data=dict()
    with connector.connection.cursor(dictionary=True) as cursor:
        query="Select * from session_details"
        cursor.execute(query)
        data=cursor.fetchall()
    
    context={'session_details':data}

    return render(request,'aapHome.html',context)

def sessionAjax(request):
    faculty_id=request.session.get('facultyId')
    session_id=request.POST.get('session')

    connector=DbConnector()
    data=dict()
    with connector.connection.cursor(dictionary=True) as cursor:
        query="SELECT course_details.course_id,course_details.course_name,course_details.course_code from course_details JOIN teaches WHERE teaches.course_id=course_details.course_id and teaches.session_id=%s and teaches.faculty_id=%s;"

        cursor.execute(query,(session_id,faculty_id))
        data=cursor.fetchall()
        print(type(data))
        print(data)
    length_of_data=len(data)
    context=dict()
    return JsonResponse(data, safe=False)