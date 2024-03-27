# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from store.models import Products
from store.models import Cart

# @login_required
def product_list(request):
		products = Products.objects.all()
		cart_count = Cart.objects.filter(user=request.user).count()
		return render(request, 'product_list.html',{'products':products,'cart_count':cart_count})