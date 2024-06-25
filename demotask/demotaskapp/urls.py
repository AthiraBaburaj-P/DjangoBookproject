from django.contrib import admin
from django.urls import path
from . import views
app_name='demotaskapp'


urlpatterns = [

    path('',views.demo, name='demo'),
    # path('opr/',views.operation,name='operation'),
    # path('contact/',views.contact,name='contact'),
    
]
