from django.contrib import admin
from .models import Product, Category, ItemModel, Student

# Register your models here.
admin.site.register(ItemModel)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id",'name',"desc", "category"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "city", "photo"]
