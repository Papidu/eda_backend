from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from dishes.views import DishesViewSet, CategoryViewSet

router = SimpleRouter()
router.register(r'api/dishes', DishesViewSet)
router.register(r'api/category', CategoryViewSet)
urlpatterns = [
    # url(r'dishes', DishesViewSet, name='dishes')
]

urlpatterns += router.urls
