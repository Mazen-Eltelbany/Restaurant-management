from django.urls import path
from .views import *

urlpatterns=[
    path('',menus,name='menu'),
    path('add/',addmeal,name='addmeal'),
    path('delete/<int:id>/',deletemeal,name='deletemeal'),
    path('update/<int:id>/',updatemeal,name='updatemeal'),
]