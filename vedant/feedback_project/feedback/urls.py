from  .import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),  # Handles the empty path "/"
    path('feedback_form/', views.feedback_view, name='feedback_form'),
    path('thank_you/', views.thank_you, name='thank_you'),
]