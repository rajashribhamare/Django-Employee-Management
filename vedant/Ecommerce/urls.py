from django.contrib import admin
from django.urls import path

from .views import ProductListView, CategoryListView, BrandListView

urlpatterns=[
    path("admin/", admin.site.urls),
    path("product/",ProductListView.as_view()),
    path("Category/",CategoryListView.as_view()),
    path("Brand/",BrandListView.as_view()),

]