from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product

# def product(requests, product_id):
#     product = get_object_or_404(Products, pk=product_id)
#     context = {
#         "product": product,
#     }
#     return render(request, "pages/cart.html", context)


def cart2(request):
    # pass
    context = {
        
    }
    return render(request, "pages/cart.html", context)

def cart(request, product_id):
    print("product_id ", product_id)
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    context = {
        "products": product,
    }
    return render(request, 'pages/cart.html', context)


    