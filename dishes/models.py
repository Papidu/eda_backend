from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    required = models.BooleanField(blank=True)
    additional = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name_plural = 'Ингридиенты'


class CategoryDishes(models.Model):
    type_dishes = models.CharField(max_length=80,)

    def __str__(self):
        return f"{self.type_dishes}"

    class Meta:
        verbose_name_plural = 'Категории'


class Dishes(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category_type = models.ForeignKey(CategoryDishes, null=True, blank=True, on_delete=models.SET_NULL)
    img = models.ImageField(blank=True)
    description = models.TextField()
    ingredient = models.ManyToManyField(Ingredients, blank=True)
    is_new = models.BooleanField(blank=True, null=True)
    # count_dishes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name_plural = 'Блюда'


#python manage.py runserver 10.241.13.136:8000