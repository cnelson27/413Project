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
            item = cmod.SaleItem.objects.get(id=product.id)
            if item is None:
                item = cmod.SaleItem()
                item.status = "A"
                item.product = theproduct
                item.price = theproduct.price
                item.sale = cart
                item.quantity = form.cleaned_data.get('quantity')
                item.save()
            else:
                item.quantity = form.cleaned_data.get('quantity')

            
            # If form is valid, create or get the user's 
            # shopping cart Sale object (purchased=None), 
            # add a SaleItem record, and 
            return HttpResponseRedirect('/catalog/cart/', {
                'cart' : cart,
            })
        # check all the variables
        # we assume the user does it wrong
        # if user did do it right:
        # do the work (reset password, create account, finalize the sale)
        #return HttpResponseRedirect(homepage/contact/)
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
    product = forms.HiddenInput

    def clean(self):
        quantity=self.cleaned_data.get('quantity')
        if quantity > self.product.quantity:
            raise forms.ValidationError('Quantity not available')
        if quantity <= 0:
            raise forms.ValidationError('Please enter a positive quantity')
        return self.cleaned_data


    