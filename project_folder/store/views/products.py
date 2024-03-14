from django.shortcuts import render
from store.models import Products


def product_list(request):
		products = Products.objects.all()
		return render(request, 'product_list.html',{'products':products})