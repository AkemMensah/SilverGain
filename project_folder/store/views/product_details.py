from django.shortcuts import render
from store.models.products import Products

def product_details(request,product_id):
    product= Products.objects.filter(pk=product_id).first()
    if product:
        similar= Products.objects.filter(category=product.category).exclude(pk=product.pk)
        return render(request,'product_details.html',{"product":product,"similar":similar})
    else:
        return render(request,'product_Notfound.html',{"product":product})