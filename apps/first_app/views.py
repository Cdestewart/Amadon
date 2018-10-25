from django.shortcuts import render, HttpResponse, redirect

from .models import Orders
def index(request):
    return render(request, "first_app/index.html", )

def show(request):
    cart= Orders.objects.all().values()
    total = 0
    count = 0
    for x in cart:
        total += x['price']*x['quant']
        count +=(1*x['quant'])
    bought ={
        'total' : total,
        'count' : count,
        'last'  : Orders.objects.last().price*Orders.objects.last().quant
    }
    return render(request, "first_app/cart.html", bought)

def buy(request):
    items = {
        '1001': {'item': 'tshirt', 'price':19.99},
        '1402': {'item': 'sweater', 'price':29.99},
        '2102': {'item': 'cup', 'price':4.99},
        '4193': {'item': 'book','price':49.99}
    }
    order_id = request.POST['code']

    Orders.objects.create(item =items[order_id]['item'], price = items[order_id]['price'], quant = request.POST['quantity'])
    return redirect('/amadon/cart')