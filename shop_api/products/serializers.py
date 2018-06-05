from rest_framework import routers, serializers, viewsets
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('pk', 'title', 'description', 'price')
