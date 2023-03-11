from django.db import models
from djongo import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from bson import ObjectId

# Create your models here.
class User(AbstractBaseUser):
    def validate_file_size(value):
        max_size = 1024 * 1024  # 1MB in bytes
        if value.size > max_size:
            raise ValidationError(f"File size exceeds {max_size} bytes.")
        
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50,unique=True)
    password        = models.CharField(max_length=100)
    phone_number    = models.IntegerField(null=True,blank=True)
    User_id         = models.IntegerField(primary_key=True)
    profile_img     = models.FileField(null = True,upload_to='Uploads/user/profile',validators=[validate_file_size])
    is_order        = models.BooleanField(default=None)
    
    USERNAME_FIELD = 'username'

class Add_product(models.Model):
    Product_name   = models.CharField(max_length=50)
    Price          = models.IntegerField()
    Quantity       = models.IntegerField()
    Product_img    = models.FileField(null=True,upload_to='Uploads/user/profile')


    

    