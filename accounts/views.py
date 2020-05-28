from django.shortcuts import render, redirect
from accounts.models import *
from .forms import OrderForm


def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    return render(request, 'accounts/dashboard.html', {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    })


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {
        'products': products
    })


def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    order_count = orders.count()
    return render(request, 'accounts/customer.html', {
        'customer': customer,
        'orders': orders,
        'order_count': order_count
    })


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderForm()

    context = {'form': form}
    return render(request, 'accounts/create_order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'accounts/update_order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('index')

    context = {'order': order}
    return render(request, 'accounts/delete_order.html', context)
