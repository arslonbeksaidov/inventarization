from django.contrib import admin
from .models import Category, Product, Room, Inventory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'category', 'unit']
    search_fields = ['name', 'sku']
    list_filter = ['category']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    list_filter = ['floor']
    search_fields = ['name']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'room', 'quantity']
    list_filter = ['room', 'product']
    search_fields = ['product__name', 'room__name']
