from specific.views import *
from django.urls import path 
app_name='specific'
urlpatterns=[
    path('ntr/',ntr,name='ntr'),
    path('dhoni/',dhoni,name='dhoni'),
]