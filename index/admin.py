from django.contrib import admin
from .models import Type, Product

# Register your models here.
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'size', 'weight', 'type']
    
