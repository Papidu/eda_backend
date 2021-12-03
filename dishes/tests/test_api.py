from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dishes.models import Dishes
from dishes.serialezers import DishesSerializer


class DishesTestCase(APITestCase):
    def setUp(self) -> None:
        self.dish_1 = Dishes.objects.create(name='Coffee', price=150, type_dishes='Напитки',
                                            description='asdasdasda')
        self.dish_2 = Dishes.objects.create(name='Капучино', price=150.00, type_dishes='Напитки',
                                            description='Aроматный свежий капучино')
        self.dish_3 = Dishes.objects.create(name='Суп', price=100.00, type_dishes='Супы',
                                            description='огда совсем нет времени,')
        self.dish_4 = Dishes.objects.create(name='Суп', price=250.00, type_dishes='Супы',
                                            description='Суп харчо из говядины с рисом — знаменитое блюдо')

    def test_get(self):
        url = reverse('dishes-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        serializer_data = DishesSerializer([self.dish_1, self.dish_2, self.dish_3, self.dish_4], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('dishes-list')
        response = self.client.get(url, data={'price': 150.0})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        serializer_data = DishesSerializer([self.dish_1, self.dish_2], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('dishes-list')
        response = self.client.get(url, data={'search': 'Суп'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        serializer_data = DishesSerializer([self.dish_3, self.dish_4], many=True).data
        self.assertEqual(serializer_data, response.data)
