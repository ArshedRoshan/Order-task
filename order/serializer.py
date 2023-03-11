from rest_framework import serializers
from.models import Order_product

class OrderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    # quantity = serializers.IntegerField()
    class Meta:
        model = Order_product
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            "UserID": data["user_id"],
            "Order_id": data["order_id"],
            "status": instance.status,
            "Updated_order_date_time": instance.updated_at.strftime('%d-%m-%Y %I:%M %p')
        }