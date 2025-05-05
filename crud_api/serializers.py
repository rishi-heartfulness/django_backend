# serializers.py

from rest_framework import serializers
from .models import Product,PaymentMode, CustomUser

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description', 'stock']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = CustomUser.objects.filter(email=email).first()
        if user and user.check_password(password):
            data["user"] = user
            return data
        raise serializers.ValidationError("Invalid email or password")



class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    payment_mode = serializers.ChoiceField(choices=PaymentMode.values)
    orders = OrderItemSerializer(many=True)  

