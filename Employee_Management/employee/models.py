from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
