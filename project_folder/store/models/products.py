from django.db import models
from .category import Category
from django.db.models import Avg

# Create your models here.
class Products (models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    quantity = models.SmallIntegerField(default=1000)
    class Meta:
        verbose_name_plural = "Products"

    @property
    def review_count(self):
        return self.reviews.count()
    @property
    def average_review(self):
        average_rating = self.reviews.aggregate(average_rating=Avg('stars'))['average_rating']
        return f'{average_rating:.1f}' if average_rating else ""
    
    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
 
    @staticmethod
    def get_all_products():
        return Products.objects.all()
 
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if isinstance(category_id, int):
            return Products.objects.filter(category_id=category_id)
        else:
            raise TypeError("Category_Id must be an integer")
