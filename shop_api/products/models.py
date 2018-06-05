from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    price = models.IntegerField()
