from django.shortcuts import render


def home(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)

def login(request):
    template = 'login.html'
    context = {}
    return render(request, template, context)

def cart(request):
    template = 'cart.html'
    context = {}
    return render(request, template, context)

def customer(request):
    template = 'customer.html'
    context = {}
    return render(request, template, context)

def empty(request):
    template = 'empty.html'
    context = {}
    return render(request, template, context)

def register(request):
    template = 'register.html'
    context = {}
    return render(request, template, context)

def payment(request):
    template = 'payment.html'
    context = {}
    return render(request, template, context)

def shipping(request):
    template = 'shipping.html'
    context = {}
    return render(request, template, context)

def categories(request):
    template = 'categories.html'
    context = {}
    return render(request, template, context)

def products(request):
    template = 'products.html'
    context = {}
    return render(request, template, context)