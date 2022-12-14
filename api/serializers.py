from rest_framework.serializers import ModelSerializer
from .models import Meal, Rating
from rest_framework import serializers

class MealSerializer(ModelSerializer):
    class RatingUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = Rating
            fields = ['stars']
    rating = RatingUserSerializer(many=True, read_only=True, source='rating_set')        
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description','rating']

class RatingSerializer(ModelSerializer):
    
    class Meta:
        model = Rating
        fields = ['id','stars','user', 'meal']