# Core
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Project file imports
from accounts.models import *
from .forms import OrderForm, RegistrationForm
from .filters import OrderFilter
from .decorators import *


@login_required(login_url='login')
@admin_only
def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    return render(
        request, 'accounts/dashboard.html', {
            'orders': orders,
            'customers': customers,
            'total_customers': total_customers,
            'total_orders': total_orders,
            'delivered': delivered,
            'pending': pending
        })


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'order_filter': order_filter
    }
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    context = {
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('index')

    context = {'order': order}
    return render(request, 'accounts/delete_order.html', context)


@unauthorized_user
def loginView(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username and Password is incorrect.')

    return render(request, 'accounts/login.html')


@unauthorized_user
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, f'Account has  been successfully created for {user}')
            # return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def logoutView(request):
    logout(request)

    return redirect('login')
