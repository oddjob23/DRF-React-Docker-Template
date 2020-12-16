from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()