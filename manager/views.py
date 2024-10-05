from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, Createuser
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    tags = Tag.objects.all()

    total_customers = customers.count()
    pend = orders.filter(status='pending').count()
    out = orders.filter(status='out of delivery').count()
    deli = orders.filter(status='delivered').count()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    

    context = {
        'customers': customers, 
        'products': products,
        'myfilter': myfilter,
        'orders': orders,
        'tags': tags,
        'no_c': total_customers,
        'no_p': pend,
        'no_o': out,
        'no_d': deli,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def customer(request, pk):
    customer =Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    return render(request, 'another.html', {'customer':customer, 'orders': orders})

@login_required(login_url='login')
def order(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        return render(request, 'order_form.html', {'form': form})
    
@login_required(login_url='login')
def update(request, pk):
    info = Order.objects.get(id=pk)
    form = OrderForm(instance=info)

    context = {
        'form': form
    }
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('/')
    else: 
        return render(request, 'update.html', context)
        
@login_required(login_url='login')   
def delete(request, pk):
    info = Order.objects.get(id=pk)
    
    context = {
        'item': info
    }
    if request.method == 'POST':
        info.delete() 
        return redirect('/')
    else: 
        return render(request, 'delete.html', context)
    
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'password or username is incorrect')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return render(request, 'login.html')

def register(request):
    form = Createuser()

    if request.method == 'POST':
        form = Createuser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile details updated')
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'register.html', context)