from django.shortcuts import render
import uuid
from django.shortcuts import render
from .serializer import Userserializer,Productserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

# Create your views here.
@api_view(['GET','POST'])
def signup(request):
    user_data = request.data
    user_data['User_id'] = random.randint(100000, 999999)
    serializer = Userserializer(data=request.data,partial = True)
    if serializer.is_valid() :
        serializer.save()
        return Response(200)
    return Response(serializer.errors)

@api_view(['GET','POST'])
def add_product(request):
    serializer = Productserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(200)
    return Response(serializer.errors)
    
    
    