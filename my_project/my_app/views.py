from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello, this is my first Django view!")