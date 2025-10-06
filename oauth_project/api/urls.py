from django.urls import path
from .views import public_api, protected_api

urlpatterns = [
    path('public/', public_api, name='public_api'),
    path('protected/', protected_api, name='protected_api'),
]
