from django.db import models

# Create your models here.
class ItemModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=False)
    price = models.IntegerField

    class Meta:
        verbose_name_plural = "Item Modal"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    photo = models.ImageField(upload_to="picture/",max_length=254)
    city = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Student Information"

    def __str__(self):
        return self.name