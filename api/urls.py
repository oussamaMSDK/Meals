from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('meals',views.MealViewSet, basename='meals')
router.register('rating', views.RatingViewSet, basename='rating')

urlpatterns = [
    
]+router.urls
