from .views import EmployeeListCreate
from django.urls import path

urlpatterns =[
    path('employee/',EmployeeListCreate.as_view(),name='employee-list-create')
]
