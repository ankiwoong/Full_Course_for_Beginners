from django.shortcuts import render

from .forms import ProductForm
from .models import Product

# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # Initialize form content

    context = {"form": form}

    return render(request, "products/product_create.html", context)  # In App Template


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    # }
    context = {"object": obj}
    # return render(request, "product/detail.html", context)  # Out App Template
    return render(request, "products/product_detail.html", context)  # In App Template
