# Generated by Django 4.2.11 on 2024-03-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_customer_order_products_delete_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]