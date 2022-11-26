from rest_framework import serializers
from .models import ItemModel, Product, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "roll", "city", "photo"]

# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=200)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     class Meta:
#         model = Student
#         fields = ['id', "name", "roll", "city"]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ["id", 'name', 'price']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = ('id', 'desc')