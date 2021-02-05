from django.shortcuts import render
from .models import Sellpost
# Create your views here.
from django.http import HttpResponse


def index(request):

    if request.method == "POST":
        product_name = request.POST.get('product_name', '')
        category = request.POST.get('category', '')
        subcategory = request.POST.get('subcategory', '')
        price = request.POST.get('price', '')
        phone = request.POST.get('phone', '')
        image=request.POST.get('image','')
        desc = request.POST.get('desc', '')
        sellpost = Sellpost(product_name=product_name, category=category,subcategory=subcategory,price=price,phone=phone,image=image,desc=desc)
        sellpost.save()
    
    return render(request, 'seller/index.html')