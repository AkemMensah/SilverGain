from django.db import models

class Cart(models.Model):
    product = models.ForeignKey('store.Products',on_delete=models.CASCADE,related_name="cart")
    quantity = models.IntegerField(default=1)
