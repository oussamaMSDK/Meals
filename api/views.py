from django.shortcuts import render
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer
from rest_framework.viewsets import ModelViewSet
from  django.views import generic
# Create your views here.


class MealViewSet(ModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

class RatingViewSet(ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
