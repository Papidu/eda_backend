from django.contrib import admin

# Register your models here.
from dishes.models import Dishes, Ingredients, CategoryDishes

admin.site.register(Dishes)
admin.site.register(Ingredients)
admin.site.register(CategoryDishes)
