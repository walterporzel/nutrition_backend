from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('foods', views.FoodList.as_view(), name='food_list'),
    path('foods/<int:pk>', views.FoodDetail.as_view(), name='food_detail'),
]