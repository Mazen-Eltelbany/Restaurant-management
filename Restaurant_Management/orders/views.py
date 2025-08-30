from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from .models import Orders
from customers.models import Customers
from menu.models import MenuItem
def allorders(request):
    context={}
    context['orders']=Orders.GetallOrders()
    return render(request,'orders/orders.html',context)
def addorder(request):
    if request.method == 'POST':
        customer_id = request.POST.get('cust_name')
        phone = request.POST.get('phone')
        meal_id=request.POST.get("meal")
        quantity=request.POST.get("qun")
        customer = Customers.objects.get(id=customer_id)
        meal=MenuItem.GetMealById(id=meal_id)
        o = Orders(
                customer=customer, 
                customer_name=customer.name, 
                phone=phone,
                quantity=quantity,
                item=meal
            )
        o.save()
        return redirect('allorders')
    customers = Customers.objects.all()
    meal=MenuItem.GetAllMeals()
    return render(request, 'orders/addorder.html', {'customers': customers,"menu":meal})
def deleteorder(request,id):
    Orders.objects.filter(id=id).delete()
    return redirect("allorders")
def updateorder(request,id):
    o=Orders.GetOrderById(id)
    if request.method=='POST':
        customer_id=request.POST.get('cust_name')
        phone=request.POST.get('phone')
        meal_id=request.POST.get('meal')
        customer=Customers.GetCustomerbyid(id=customer_id)
        meal=MenuItem.GetMealById(id=meal_id)
        quantity=request.POST.get('qun')
        o.customer=customer
        o.customer_name=customer.name
        o.phone=phone
        o.item=meal
        o.quantity=quantity
        o.save()
        return redirect("allorders")
    customer=Customers.GetallCustomers()
    meal=MenuItem.GetAllMeals()
    return render(request,'orders/updateorder.html',{"customer":customer,"menu":meal,"order":o})


