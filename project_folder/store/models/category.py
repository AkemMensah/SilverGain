from django.db import models
 
 
class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Categories"
 
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
 
    def __str__(self):
        return self.name