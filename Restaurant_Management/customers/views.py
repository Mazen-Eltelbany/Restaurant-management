from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customers
from orders.models import Orders
def showmainpage(request):
    return render(request,'base.html')
def allcustomers(request):
    context={}
    context['customers']=Customers.GetallCustomers()
    return render(request,'customers/customers.html',context)
def addcustomer(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        c=Customers(name=name,phone=phone,email=email)
        c.save()
        return redirect('customers')#redirect with name of url
    return render(request,'customers/add.html')
def deletecustomer(request,id):
    Customers.objects.filter(id=id).delete()
    return redirect('customers')
def updatecustomer(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        c=Customers(id=id,name=name,phone=phone,email=email)
        c.save()
        return redirect('customers')
    return render(request,'customers/update.html')
# def customerorders(request,id):
#     context={}
#     context['orders']=Orders.objects.filter(customer_id=id)
#     return render(request,'customers/customerorders.html',context)
