from django.shortcuts import render
from django.views.generic import ListView
from .models import books

# Create your views here.
class booksListView(ListView):
    queryset = books.objects.all()