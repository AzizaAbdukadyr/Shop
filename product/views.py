from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *

menu = ['О магазине', 'Каталог', 'Заказы', 'Контакты']
product = ['Футболки/рубашки', 'Брюки', 'Обувь']


class ListProduct(ListView):
    model = Product
    template_name = 'product/main_page.html'
    context_object_name = 'prod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Каталог'
        return context


# def main_page(request):
#     prod = Product.objects.all()
#     return render(request, 'product/main_page.html', {'prod': prod, 'menu': menu, "title": "Главная стр."})


# def catalog(request):
#     return render(request, "product/catalog.html", {'product': product, "title": "Каталог"})


# def catalog(request, catid):
#     return HttpResponse(f"<h1>Каталог</h1><p>{catid}</p>")