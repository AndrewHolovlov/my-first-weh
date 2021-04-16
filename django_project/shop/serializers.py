from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'price', 'type_id', 'publish_date')
















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