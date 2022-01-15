from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    required = models.BooleanField(blank=True, verbose_name='Обязательное поле')
    additional = models.BooleanField(blank=True, verbose_name='Дополнительный')

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = 'Ингридиенты'
        verbose_name_plural = 'Ингридиенты'


class CategoryDishes(models.Model):
    type_dishes = models.CharField(max_length=80, verbose_name='Тип категории')

    def __str__(self):
        return f"{self.type_dishes}"

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Dishes(models.Model):
    name = models.CharField(max_length=255, verbose_name='Нащвание блюда')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    category_type = models.ForeignKey(CategoryDishes, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Тип категории')
    img = models.ImageField(blank=True, verbose_name='Фото блюда')
    description = models.TextField(verbose_name='Описание')
    ingredient = models.ManyToManyField(Ingredients, blank=True, verbose_name='Ингредиенты')
    is_new = models.BooleanField(blank=True, null=True, verbose_name='Новое')
    # count_dishes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = 'Блюда'
        verbose_name_plural = 'Блюда'


#python manage.py runserver 10.241.13.136:8000