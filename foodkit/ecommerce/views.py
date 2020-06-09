from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone

from .models import Item, OrderItem, Order

# Create your views here.
class InicioView(ListView):
    model = Item
    template_name = "ecommerce/inicio.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "ecommerce/producto.html"

def productos(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "ecommerce/productos.html", context)

def checkout(request):
    return render(request, "ecommerce/checkout.html")

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Producto añiadido al carrito de compra.")
            return redirect("ecommerce:producto", slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "Producto añiadido al carrito de compra.")
            return redirect("ecommerce:producto", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Producto añiadido al carrito de compra.")
        return redirect("ecommerce:producto", slug=slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "Producto removido del carrito de compra.")
            return redirect("ecommerce:producto", slug=slug)
        else:
            messages.info(request, "Este producto no estaba en el carrito de compra.")
            return redirect("ecommerce:producto", slug=slug)
    else:
        messages.info(request, "Usted no posee una orden activa.")
        return redirect("ecommerce:producto", slug=slug)
