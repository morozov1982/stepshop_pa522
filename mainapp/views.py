from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'Главная'

    prods = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': prods,
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)

def about(request):
    title = 'О нас'
    context = {
        'title': title,
    }
    return render(request, 'about.html', context)

def products(request):
    title = 'Товары'
    context = {
        'title': title,
    }
    return render(request, 'products.html', context)

def product(request):
    title = 'Товар'
    context = {
        'title': title,
    }
    return render(request, 'product.html', context)
