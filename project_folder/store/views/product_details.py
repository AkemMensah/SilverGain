from django.shortcuts import render
from store.models.products import Products
from store.models.cart import Cart

def product_details(request,product_id):
    product= Products.objects.filter(pk=product_id).first()
    cart_count = Cart.objects.filter(user=request.user).count()
    if product:
        similar= Products.objects.filter(category=product.category).exclude(pk=product.pk)
        return render(request,'product_details.html',{"product":product,"similar":similar,"cart_count":cart_count})
    else:
        return render(request,'product_Notfound.html',{"product":product})