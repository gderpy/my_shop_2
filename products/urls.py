from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path('', views.index, name='home'),
    path("categories/", views.categories, name="categories"),
    path('catalog/<slug:cat_slug>', views.category_detail, name='cat_catalog'),
    path('product/<slug:product_slug>', views.product_detail, name="product_detail"),
]

