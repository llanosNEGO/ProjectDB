
from django.urls import path
from . import views

urlpatterns = [

    path('',views.hello),
    path('segunda/',views.segunda),
    path('index/',views.index),
    
]