from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.core.exceptions import ValidationError
from catalog import models as cmod
from django import forms
from account import models as amod

@view_function
def process_request(request, product):
    theproduct = cmod.Product.objects.get(id=product)
    thumbnails = theproduct.image_urls()
    featured = thumbnails[0]
    del thumbnails[0]
    if request.method == "POST":
        form = buyForm(request.POST)
        form.user = request.user
        form.product = cmod.Product.objects.get(id=product)
        if request.user.is_authenticated == False:
            return HttpResponseRedirect('/account/login/')
        if form.is_valid():
            cart = request.user.get_shopping_cart()
            if not cmod.SaleItem.objects.filter(sale=cart,product=theproduct).exists():
                cartItem = cmod.SaleItem()
                cartItem.status = "A"
                cartItem.product = theproduct
                cartItem.price = theproduct.price
                cartItem.sale = cart
                cartItem.quantity = form.cleaned_data.get('quantity')
                cartItem.save()
            else:
                cartItem = cmod.SaleItem.objects.get(sale=cart, product=theproduct)
                if cartItem.status =='A':
                    cartItem.quantity += form.cleaned_data.get('quantity')
                else:
                    cartItem.status = 'A'
                    cartItem.quantity = form.cleaned_data.get('quantity')
                cartItem.save()
            return HttpResponseRedirect('/catalog/cart/')
    else: 
        form = buyForm()
        form.product = product
    return request.dmp.render('product.html', {
        'product' : theproduct,
        'thumbnails' : thumbnails,
        'featured' : featured,
        'form' : form,
    })


@view_function
def tile(request, product):
    theproduct = cmod.Product.objects.get(id=product)
    return request.dmp.render('product.tile.html', {
        'product' : theproduct,
    })

class buyForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity')

    def clean(self):
        quantity=self.cleaned_data.get('quantity')
        if quantity > self.product.quantity:
            raise forms.ValidationError('Quantity not available')
        if quantity <= 0:
            raise forms.ValidationError('Please enter a positive quantity')
        return self.cleaned_data


    