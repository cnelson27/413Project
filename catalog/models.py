from django.db import models

# Create your models here.

class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()

class Product(models.Model):
    category = Category(models.ForeignKey)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(db_index=True, choices='Active' or 'Inactive' default='Active')
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2
    #quantity refers to current in stock
    quantity = models.IntegerField()
    # reorder_trigger refers to when we reorder
    reorder_trigger = models.IntegerField()
    # reorder_quantity refers to how many we order
    reorder_quantity = models.IntegerField()