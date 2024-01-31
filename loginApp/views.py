from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth import logout
from dbConnection.dbConnectionClass import DbConnector

# Create your views here.

def loginPage(request):
    # response="<h1>Hello Django</h1>"
    # template=loader.get_template('alogin.html')
    # response=template.render()
    # return HttpResponse(response)
    return render(request,'login.html')

def aloginajax(request):
    userId=request.POST.get("userid")
    password=request.POST.get("password")

    data=dict()
    connector=DbConnector()
    with connector.connection.cursor(dictionary=True) as cursor:
        query="Select * from admin_details where admin_userid= %s and admin_password= %s"
        cursor.execute(query,(userId,password))
        data=cursor.fetchall()

    if not data:
        status={'status':"NOT OK"}
        request.session.flush()
        return JsonResponse(status)
    else:   
        if(request.method=="POST" and userId==data[0]['admin_userid']and password==data[0]['admin_password']):
            status={"status":"OK"}
            request.session['adminName']=data[0]['admin_name']
            return JsonResponse(status)
        else:
            status={'status':"NOT OK"}
            request.session.flush()
            return JsonResponse(status)


def floginajax(request):
    userId=request.POST.get("userid")
    password=request.POST.get("password")

    data=dict()
    connector=DbConnector()
    with connector.connection.cursor(dictionary=True) as cursor:
        query="Select * from faculty_dept where faculty_userid=%s and faculty_password=%s"
        cursor.execute(query,(userId,password))
        data=cursor.fetchall()

    if not data:
        status={'status':"NOT OK"}
        request.session.flush()
        return JsonResponse(status)
    else:   
        if(request.method=="POST" and userId==data[0]['faculty_userid']and password==data[0]['faculty_password']):
            status={"status":"OK"}
            request.session['facultyName']=data[0]['faculty_name']
            request.session['designation']=data[0]['faculty_designation']
            request.session['facultyId']=data[0]['faculty_id']
            request.session['facultyDept']=data[0]['faculty_name']
            request.session['facultySchool']=data[0]['faculty_name']
            return JsonResponse(status)
        else:
            status={'status':"NOT OK"}
            request.session.flush()
            return JsonResponse(status)
    
def ahome(request):
    # if request.method=="POST":
    if bool(request.session ):
        username=request.session.get('adminName')
        return render(request,'ahome.html',{'username':username})
    else:
        error_msg="Error: Please login First"
        return HttpResponse(error_msg)
        # return render(request,error_msg)

def fhome(request):
    if request.session.get('facultyName') is None:
        error_msg="Error: Please login First"
        return HttpResponse(error_msg)
        # return render(request,error_msg)

    else:
        
        # username=request.session.get('facultyName')
        # return render(request,'fhome.html',{'username':username})

        context={"username":request.session.get('facultyName'),"designation": request.session.get('designation'),"faculty_id": request.session.get('facultyId'),"faculty_dept": request.session.get('facultyDept'),"faculty_school": request.session.get('facultySchool'),}

        return render(request,'fhome.html',context)
    
     
def logout(request):
    # return redirect('login.html')  # Change 'login' to your actual login page URL
        request.session.flush()
        print(request.session.get('facultyName'))
        print("Logged out")
        response = HttpResponseRedirect(reverse(loginPage))
        response.delete_cookie('sessionid')
        return response
