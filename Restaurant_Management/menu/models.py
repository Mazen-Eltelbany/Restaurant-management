from django.db import models

class MenuItem(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    @classmethod
    def GetAllMeals(cls):
        return cls.objects.all()
    @classmethod
    def GetMealById(cls,id):
        return cls.objects.get(id=id)
