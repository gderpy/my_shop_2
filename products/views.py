from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def index(request):
    return render(request, 'products/index.html')


def categories(request):
    categories = Category.main_categories.all()

    data = {
        "categories": categories,
    }

    return render(request, "products/categories.html", context=data)


def catalog(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    list_product = category.products.all()  # Используем related_name и Product

    data = {
        "products": list_product,
    }

    return render(request, "products/cat_catalog.html", context=data)
