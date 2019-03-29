from django.db import models
from catalog import models as cmod
from Project1 import settings
from decimal import Decimal
import datetime
import stripe


TAX_RATE = Decimal("0.05")

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

    def image_url(self):
        
        return self.image_urls()[0]

    def image_urls(self):
        urls = []
        for pi in ProductImage.objects.filter(product=self):
            urls.append(pi.image_url())
        if len(urls) == 0:
            urls.append(settings.STATIC_URL + 'catalog/media/products/notfound.jpg')
        return urls



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filename = models.TextField()
    

    def image_url(self):
        return (settings.STATIC_URL + 'catalog/media/products/' + self.filename)

class Sale(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    purchased = models.DateTimeField(null=True, default=None)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe

    def recalculate(self):
        
        self.subtotal = Decimal("0")
        saleItems = SaleItem.objects.filter(sale=self, status='A')
        for saleItem in saleItems:
            self.subtotal += (saleItem.price * saleItem.quantity)
        self.tax = Decimal(str(self.subtotal * TAX_RATE)).quantize(Decimal('0.01'))
        self.total = Decimal(str(self.subtotal + self.tax)).quantize(Decimal('0.01'))
        # self.tax = (self.subtotal * TAX_RATE)
        # self.total = (self.subtotal + self.tax)
        '''Recalculates the subtotal, tax, and total fields. Does not save the object.'''
        # complete this method!

    def finalize(self, stripeToken):
        '''Finalizes the sale'''
        if self.purchased is not None:
            raise ValueError('This sale has already been finalized')
        saleItems = SaleItem.objects.filter(sale=self, status='A')
        for saleItem in saleItems:
            if saleItem.quantity > saleItem.product.quantity:
                raise ValueError(saleItem.product.name + ': We only have ' + str(saleItem.product.quantity) + ' in stock.')
        self.recalculate()
        charge = stripe.Charge.create(
            amount = int(self.total * 100),
            currency='usd',
            description='Example charge',
            source=stripeToken,
        )
        # charge = stripe.Charge.create(
        #     amount=999,
        #     currency='usd',
        #     description='Example charge',
        #     source=token,
        # )
        self.charge_id = charge['id']
        # charge.save()
        self.purchased = datetime.datetime.now()
        
        self.save()

        for saleItem in saleItems:
            saleItem.product.quantity -= saleItem.quantity
            saleItem.product.save()
        
        # self.charge_id = 

        # complete this method!
        # Ensure this sale isn't already finalized (purchased should be None)
        # Check product quantities one more time
        # Call recalculate one more time
        # Create a charge using the `stripeToken` (https://stripe.com/docs/charges)
            # be sure to pip install stripe and import stripe into this file
        # Set purchased=now and charge_id=the id from Stripe
        # Save


class SaleItem(models.Model):
    STATUS_CHOICES = [
        ( 'A', 'Active' ),
        ( 'D', 'Deleted' ),
    ]
    status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    class Meta:
        ordering = [ 'product__name' ]