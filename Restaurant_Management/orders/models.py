from django.db import models
from customers.models import Customers
from menu.models import MenuItem
class Orders(models.Model):
        customer=models.ForeignKey(Customers,on_delete=models.CASCADE,related_name="orders")
        item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
        customer_name=models.CharField(max_length=50)
        phone=models.CharField(max_length=15)
        created_at = models.DateTimeField(auto_now_add=True)
        quantity=models.PositiveIntegerField()
        @classmethod
        def GetallOrders(cls):
                return cls.objects.all()
        @classmethod
        def GetOrderById(cls,id):
                return cls.objects.get(id=id)
