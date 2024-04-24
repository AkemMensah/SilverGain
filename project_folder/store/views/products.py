# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from store.models import Products
from store.models import Cart

# @login_required
def product_list(request):
		products = Products.objects.all()
		user = request.user if request.user.is_authenticated else None
		
		cart_count = Cart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
		return render(request, 'product_list.html',{'products':products,'cart_count':cart_count,"user":user})