from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['sku', 'name', 'category', 'price']

    def get_price(self, obj):
        discounts = []
        # 30% discount on boots
        if obj.category == "boots":
            discounts.append(30)
        # 15% discount on specific SKU
        if obj.sku == "000003":
            discounts.append(15)

        # Apply the maximum discount if applicable
        max_discount = max(discounts) if discounts else 0
        discount_amount = obj.price * max_discount // 100
        final_price = obj.price - discount_amount

        return {
            "original": obj.price,
            "final": final_price,
            "discount_percentage": f"{max_discount}%" if max_discount else None,
            "currency": "EUR"
        }
