from django.shortcuts import render
from rest_framework import generics, filters
from .models import *
from .serializers import *


# Create your views here.
class PizzaAPICreate(generics.CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaAPIView(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['size', 'type']

class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer 
