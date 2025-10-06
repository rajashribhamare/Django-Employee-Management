from django.db import models

# Create your models here.

class Employee(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.TextField()
    date_of_birth = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    