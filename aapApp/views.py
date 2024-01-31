from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import mysql.connector 
# from dbConnection.dbConnectionClass import dbConnector
from dbConnection.dbConnectionClass import create_table


# Create your views here.
def aapHome(request):
    # connect=dbConnector()
    # cursorObject=connect.conn.cursor()
    # # cursorObject.execute("create table faculty_details")
    # cursorObject.execute("CREATE TABLE IF NOT EXISTS faculty_details (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), department VARCHAR(255))")

    create_table()



    return render(request,'aapHome.html')