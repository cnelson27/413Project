from django.db import models

# Create your models here.

class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive')
    )
    status = models.TextField(
        db_index=True, 
        choices=STATUS_CHOICES,
        default='A')
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(
        max_digits=8, 
        decimal_places=2
    )
    #quantity refers to current in stock
    quantity = models.IntegerField(default=0)
    # reorder_trigger refers to when we reorder
    reorder_trigger = models.IntegerField(default=2)
    # reorder_quantity refers to how many we order
    reorder_quantity = models.IntegerField(default=5)

class ProductImage(models.Model):
    filename = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)