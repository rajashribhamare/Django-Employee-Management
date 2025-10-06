from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    description = models.TextField(max_length=100)



class Category(models.Model):
    fname = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)

class Brand(models.Model):
    name = models.CharField(max_length=100)
    Description = models.TextField(max_length=50)
    status = models.BooleanField(default=True)



