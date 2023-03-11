from django.urls import path
from user.views import *

urlpatterns = [
    path('signup',signup,name='signup'),
    path('add_product',add_product,name='add_product')
]