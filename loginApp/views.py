from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def aloginPage(request):
    # response="<h1>Hello Django</h1>"
    template=loader.get_template('alogin.html')
    response=template.render()
    return HttpResponse(response)

def aloginajax(request):
    template=loader.get_template()

