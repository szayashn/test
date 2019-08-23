from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):


    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request,id):
    
    context = {
        "order": Order.objects.get(id = id)
    }

    return render(request, "store/checkout.html",context)

def process(request):

    quantity_from_form = int(request.POST["quantity"])
    price_from_form = Product.objects.get(id = request.POST["product_id"]).price
    total_charge = quantity_from_form * price_from_form

    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge, price = price_from_form)

    order_id = Order.objects.last().id

    return redirect(f'/checkout/{order_id}')
