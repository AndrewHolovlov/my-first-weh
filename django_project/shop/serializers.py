from datetime import datetime
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.http import HttpResponse

from .models import Product, User, Order, Order_item, Contact_information


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'type_id', 'quantity', 'availability', 'price', 'discount', 'final_price', 'created_at',
                  'updated_at')

    # def update(self, instance, validated_data):
    #     instance.updated_at = datetime.now()
    #     instance.save
    #     return instance

    # def create(self, validated_data):
    #     product = Product.objects.create(**validated_data)
    #     return product


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'patronymic', 'phone')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields = ('product', 'quantity', 'order')


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_information
        fields = ('first_name', 'last_name', 'phone', 'email', 'order')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('mail_number', 'city', 'user')












# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=120)
#     quantity = serializers.IntegerField()
#     price = serializers.FloatField()
#     type_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.price = validated_data.get('price', instance.price)
#         instance.type_id = validated_data('type_id', instance.type_id)
#
#         instance.save()
#         return instance
