from django.db import models
# from store.models.products import Products

class Reviews(models.Model):
    product = models.ForeignKey("store.Products",related_name='reviews',on_delete=models.CASCADE)
    stars = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    comment = models.TextField(default="",null=True,blank=True)
