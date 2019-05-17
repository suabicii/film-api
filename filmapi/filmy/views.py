from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serialisers import FilmSerialiser, FilmFullSerialiser
from .models import Film


class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerialiser
    queryset = Film.objects.all()
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        film = self.get_object()
        serializer = FilmFullSerialiser(film)
        return Response(serializer.data)
