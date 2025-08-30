from django.urls import path
from .views import *
urlpatterns=[
    path('',allcustomers,name='customers'),
    path('add/',addcustomer,name='addcustomer'),
    path('update/<int:id>/',updatecustomer,name='updatecustomer'),
    path('delete/<int:id>/',deletecustomer,name='deletecustomer'),
]