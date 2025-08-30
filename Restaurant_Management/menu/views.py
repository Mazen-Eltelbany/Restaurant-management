from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import MenuItem
def menus(request):
    menu={}
    menu['menus']=MenuItem.objects.all()
    return render(request,'menu/menu.html',menu)
def addmeal(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get("desc")
        m=MenuItem(name=name,price=price,description=description)
        m.save()
        return redirect('menu')
    return render(request,'menu/add.html')
def deletemeal(request,id):
    MenuItem.objects.filter(id=id).delete()
    return redirect('menu')
def updatemeal(request,id):
    m=MenuItem.GetMealById(id)
    if request.method=='POST':
        m.name=request.POST.get('name')
        m.price=request.POST.get('price')
        m.description=request.POST.get('desc')
        m.save()
        return redirect('menu')
    return render(request,'menu/update.html',{'meal':m})

