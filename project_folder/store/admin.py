from django.contrib import admin
from store.models import products, category,customer,orders,reviews,cart


# Register your models here.
admin.site.register(products.Products)
admin.site.register(category.Category)
admin.site.register(customer.Customer)
admin.site.register(orders.Order)
admin.site.register(reviews.Reviews)
admin.site.register(cart.Cart)