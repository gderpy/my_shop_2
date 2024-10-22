from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import register
from django.http import HttpResponse
from .models import Product, Category


def index(request):
    return render(request, 'products/index.html')


def categories(request):
    categories = Category.main_categories.all()

    data = {
        "categories": categories,
    }

    return render(request, "products/categories.html", context=data)


def category_detail(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)

    if category.children.exists():
        subcategories = category.children.all()
        return render(request, "products/categories.html", context={"categories": subcategories})  
    else:
        products = category.products.all()
        return render(request, "products/cat_catalog.html", context={"products": products})
        

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    data = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context=data)


