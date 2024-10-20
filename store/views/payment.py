from django.shortcuts import render
from store.models.products import Products
from django.contrib.auth.decorators import login_required

@login_required
def payment(request):
    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity',1)
    payment_complete = request.GET.get('payment_complete',0)
    context = {'payment_complete':bool(int(payment_complete))}
    print(request.GET)
    # if product_id and quantity:
    product = Products.objects.get(pk=product_id)
    context['product']= product
    context['user']=request.user if request.user.is_authenticated else None
    print(context)
    
    return render(request, 'payment.html',context)