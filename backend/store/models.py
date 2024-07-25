from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    illustration = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
