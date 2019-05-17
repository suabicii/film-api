from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import FilmViewSet

router = routers.DefaultRouter()
router.register('filmy', FilmViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
