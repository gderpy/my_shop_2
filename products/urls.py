from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path('', views.index, name='home'),
    path("categories/", views.categories, name="categories"),
    path('catalog/<slug:cat_slug>', views.catalog, name='cat_catalog'),
]

