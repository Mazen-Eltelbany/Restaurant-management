from django.urls import path
from .views import *

urlpatterns=[
    path('',allorders,name='allorders'),
    path('add/',addorder,name='addorder'),
    path('delete/<int:id>',deleteorder,name='deleteorder'),
    path('update/<int:id>',updateorder,name='updateorder')
]