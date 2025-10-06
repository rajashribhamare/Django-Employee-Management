from django.urls import path
from .views import student_register, thank_you
from  .import views 
urlpatterns = [
    path('register/', student_register, name='student_register'),
    path('thank_you/', views.thank_you, name='thank_you'),
]

