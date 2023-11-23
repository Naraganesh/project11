from generic.views import *
from django.urls import path 
app_name='generic'
urlpatterns=[
    path('lokesh/',lokesh,name='lokesh'),
    path('gani/',gani,name='gani'),
]