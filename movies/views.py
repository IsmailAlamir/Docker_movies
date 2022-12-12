from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import MoviesSerializer
# Create your views here.
from .models import Movies


class MoviesListView(ListCreateAPIView):
    queryset=Movies.objects.all()
    serializer_class= MoviesSerializer


class MoviesDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Movies.objects.all()
    serializer_class= MoviesSerializer
