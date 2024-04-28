from django.urls import path
from aapApp import views

urlpatterns = [
    path('aap',views.aapHome),
    path('sessionAjax',views.sessionAjax),
]
