from django.db import models
from user.models import *

# Create your models here.
class Order_product(models.Model):
    STATUS = (
        ('Placed', 'Placed'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )
    user        = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE,null=True)
    Product     = models.ForeignKey(Add_product,related_name='add',on_delete=models.CASCADE,null=True)
    order_id    = models.CharField(max_length=11)
    ordered     = models.BooleanField(default=False)
    quantity = models.IntegerField()
    product_price = models.FloatField(null=True)
    total_amount  = models.FloatField(null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='placed')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    