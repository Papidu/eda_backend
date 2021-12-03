from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.viewsets import ModelViewSet
from dishes.models import Dishes, CategoryDishes
from dishes.serialezers import DishesSerializer, CategorySerializer


class DishesViewSet(ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']


class CategoryViewSet(ModelViewSet):
    queryset = CategoryDishes.objects.all()
    serializer_class = CategorySerializer
