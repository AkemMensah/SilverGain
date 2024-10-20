from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    product = models.ForeignKey('store.Products',on_delete=models.CASCADE,related_name="cart")
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_cart")
    class Meta:
        unique_together = ("user","product")


