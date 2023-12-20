from django.urls import path
from loginApp import views

urlpatterns = [
    path('alogin',views.aloginPage),
    path('aloginajax',views.aloginajax)
]

