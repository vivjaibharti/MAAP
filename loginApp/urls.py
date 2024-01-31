from django.urls import path
from loginApp import views

urlpatterns = [
    path('login',views.loginPage),
    path('aloginajax',views.aloginajax),
    path('floginajax',views.floginajax),
    path('ahome',views.ahome),
    path('fhome',views.fhome),
    path('logout',views.logout),
]

