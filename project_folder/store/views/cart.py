from store.models.cart import Cart
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

@login_required
def add_to_cart(request,product_id):
    try:
        cart = Cart(product_id=product_id,user=request.user)
        cart.save()
    except IntegrityError:
        pass
    return redirect('product_details',**{'product_id':product_id})
     