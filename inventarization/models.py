from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    description = models.TextField(blank=True)
    owner = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=20, default="pcs")  # e.g., pcs, kg, box

    def __str__(self):
        return f"{self.name} ({self.sku})"


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    class Meta:
        unique_together = ('product', 'room')
