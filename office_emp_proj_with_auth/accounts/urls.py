from django.urls import path
from .views import social_login_token

urlpatterns = [
    path('social/token/', social_login_token, name='social_token'),
]
