from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'serving_size', 'serving_size_unit', 'calories', 'fat', 'carbs', 'protien')