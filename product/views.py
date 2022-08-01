from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request, 'product/product.html',
                  {'Product':Product.objects.get(id=1)})
def products(request):
    pro=Product.objects.all()

    return render(request, 'product/products.html',
                  {'Products':pro})
def add_product(request):
    name = request.POST.get('name')
    print(name)
    return render(request, 'product/add_product.html')
def add(request):
    name=request.POST.get('name')
    return render(request, 'product/add_product.html')