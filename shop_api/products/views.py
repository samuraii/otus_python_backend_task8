from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from . import serializers
from . import models


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
