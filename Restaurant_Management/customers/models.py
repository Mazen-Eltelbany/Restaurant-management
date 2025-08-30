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



