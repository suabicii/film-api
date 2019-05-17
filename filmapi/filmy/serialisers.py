from rest_framework import serializers
from .models import Film


class FilmSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'poster']


class FilmFullSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'year', 'poster']
