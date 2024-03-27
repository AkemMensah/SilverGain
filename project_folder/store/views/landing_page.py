from django.shortcuts import render
from django.views import View
from store.models.products import Products

def landing_page(request):
    product1 = Products.objects.order_by('?').first()
    product2 = Products.objects.order_by('?').first()
    products = Products.objects.all()
    return render(request, 'landing_page.html',{"product1":product1,"product2":product2,"products":products})