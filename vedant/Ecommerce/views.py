from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category,Brand


# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all()


class CategoryListView(ListView):
    queryset = Category.objects.all()

class BrandListView(ListView):
    queryset = Brand.objects.all()

