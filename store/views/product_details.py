from django.shortcuts import render
from store.models.products import Products
from store.models.cart import Cart

def product_details(request,product_id):
    # product_id = request.GET.get('product_id')
    product= Products.objects.filter(pk=product_id).first()
    cart_count = Cart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    if product:
        similar= Products.objects.filter(category=product.category).exclude(pk=product.pk)
        user = request.user if request.user.is_authenticated else None
        return render(request,'product_details.html',{"product":product,"similar":similar,"cart_count":cart_count,"user":user})
    else:
        context = {'error_message':"Sorry, the product you requested was not found"}
        return render(request,'product_Notfound.html',{context})