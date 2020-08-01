from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Item, Order, OrderItem
from django.views.generic import ListView, DetailView

# Create your views here.


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item item is in the order list
        if order.items.filter(item_slug=item.slug).exists():
            order_item.quantity += 100
            order_item.save
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)

    return redirect("core:product", kwargs={
        'slug': slug
    })
  
