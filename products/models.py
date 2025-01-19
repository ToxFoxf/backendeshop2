from django.db import models

class Product(models.Model):
    nameproduct = models.CharField(max_length=20)
    price = models.IntegerField()
    amout = models.IntegerField()
    idproduct = models.IntegerField()
    typeproduct = models.CharField(max_length=20)
    
