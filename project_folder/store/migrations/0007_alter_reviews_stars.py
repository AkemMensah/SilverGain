# Generated by Django 4.2.11 on 2024-03-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='stars',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
