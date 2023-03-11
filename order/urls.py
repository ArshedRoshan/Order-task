from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('v1/order-create',create_order,name='create_order'),
    path('v1/order/<str:order_id>',order_details,name='view_order'),
    path('v1/order-update/<str:order_id>',update,name='update')
]
