# Generated by Django 4.0.6 on 2023-03-10 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_product',
            name='product_price',
        ),
    ]