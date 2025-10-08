from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet  # Make sure this matches the class name exactly

router = DefaultRouter()
router.register(r'movie', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
