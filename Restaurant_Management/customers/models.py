from django.db import models
class Customers(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    @classmethod
    def GetallCustomers(cls):
        return cls.objects.all
    @classmethod
    def GetCustomerbyid(cls,id):
        return cls.objects.get(id=id)
    def total_orders(self):
        return sum(order.quantity for order in self.orders.all())
    def total_price(self):
        return sum(order.quantity*order.item.price for order in self.orders.all())



