from rest_framework import serializers
from.models import User,Add_product

class Userserializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['first_name','last_name','username','password','phone_number','User_id','profile_img','is_order']

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Add_product
        fields = ['Product_name','Price','Quantity','Product_img']
            
        
        
