from django.shortcuts import get_object_or_404, redirect, render

from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'caatalog/index.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'caatalog/index2.html', {'product': product})


def swaggatam(request):
    return redirect('product_list')
