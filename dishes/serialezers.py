from rest_framework.serializers import ModelSerializer

from dishes.models import Dishes, CategoryDishes


class DishesSerializer(ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'
        # fields = ['name', 'type_dishes', 'img', 'price', 'id']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryDishes
        fields = ['id', 'type_dishes']
