from rest_framework import serializers

from .models import Company, Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class CompanySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
