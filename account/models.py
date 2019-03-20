from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    birthdate = models.DateTimeField(null=True)

    def get_shopping_cart(self):
        cart = cmod.Sale.objects.filter(user=self,puchased=None).first()
        if cart is None:
            cart = cmod.Sale()
            cart.user = self
        cart.recalculate()
        cart.save()

        return cart
    