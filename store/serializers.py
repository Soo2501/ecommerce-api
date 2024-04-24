import uuid

from rest_framework import serializers
from .models import Product, Discount, Category, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title"
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "title",
            "stock",
            "price",
            "description",
            "image"
        )


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (
            "id",
            "product",
            "title",
            "discount"
        )

class ProductItemSerializer(serializers.ModelSerializer):
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2, default=1)
    class Meta:
        model = Product
        fields = (
            "title",
            "category",
            "price",
            "quantity"
        )

class OrderItemSerializer(serializers.ModelSerializer):
    product_list = ProductItemSerializer(many=True, write_only=True)
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product_list",
        )

    def create(self, validated_data):
        order_items = []
        order = Order.objects.create(user=validated_data['user'])
        for order_item in validated_data.get['product_list']:
            order_item = OrderItem(
                order=order,
                **order_item
            )
            order_item.save()
            order_items.append(order_item)
        OrderItem.objects.bulk_create(order_items)
        return order_items
