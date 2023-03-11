from django.shortcuts import render
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import *
from order.serializer import *
from user.serializer import *
from django.utils import timezone
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime


# Create your views here.
@api_view(['GET','POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    request.data['order_id'] = random.randint(1000000000, 9999999999)
    print('serrr',serializer.is_valid())
    if serializer.is_valid():
        user_id = serializer.validated_data.get('user_id')
        # print('user',user_id)
        product_id = serializer.validated_data.get('product_id')
        print('product',product_id)
        user = User.objects.get(User_id = user_id)
        product = Add_product.objects.get(id=product_id)
        quantity = serializer.validated_data.get('quantity')
        product_price = product.Price
        print('quantity',quantity)
        total_amount = quantity * product_price 
        print('total',total_amount)
        order = Order_product(
            user = user,
            Product = product,
            quantity = quantity,
            total_amount = total_amount,
            product_price=product_price,
            status = 'placed',
            created_at = timezone.now(),
            updated_at = timezone.now(),
            order_id = request.data['order_id']
        )
        order.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])   
def order_details(request, order_id):
    order = get_object_or_404(Order_product, order_id=order_id)
    user = User.objects.get(User_id=order.user.User_id)
    user_data = Userserializer(user).data
    product = Add_product.objects.get(id=order.Product.id)
    product_data = Productserializer(product).data
    response_data ={
        "UserID" : user_data['User_id'],
        "Order_id":order.order_id,
        "Product_details":[
            {
            "Product_name":product_data['Product_name'],
            "Price": product_data['Price'],
            "quantity": order.quantity,
            "product_img": product_data['Product_img']
            }
            
        ],
        "Total_ammount": order.total_amount,
        "Status": order.status,
        "Order_date_time": datetime.strftime(order.created_at, "%d-%m-%Y %I:%M %p")
    }
    return Response(response_data)

@api_view(['GET','PUT']) 
def update(request,order_id):
    data = request.data
    order = Order_product.objects.get(order_id=order_id)
    data['user_id'] = order.user.User_id
    data['product_id'] = order.Product.id
    data['quantity'] = order.quantity
    data['order_id'] = order.order_id
    serializer = OrderSerializer(order,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    
    
    
    
