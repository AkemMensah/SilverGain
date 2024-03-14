from store.models.cart import Cart
from django.shortcuts import redirect

def add_to_cart(request,product_id):
    cart = Cart(product_id=product_id)
    cart.save()
    return redirect('product_details',**{'product_id':product_id})
     