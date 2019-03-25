from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.core.exceptions import ValidationError
from catalog import models as cmod
from django import forms

@view_function
def process_request(request, product):
    theproduct = cmod.Product.objects.get(id=product)
    thumbnails = theproduct.image_urls()
    featured = thumbnails[0]
    del thumbnails[0]
    if request.method == "POST":
        form = buyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/catalog/cart/')
        # check all the variables
        # we assume the user does it wrong
        print(request.POST["yourQuantity"])
        print(request.user.name)
        # if user did do it right:
        # do the work (reset password, create account, finalize the sale)
        #return HttpResponseRedirect(homepage/contact/)
    else: 
        form = buyForm()
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
    quantity = forms.CharField(label='Quantity')

        
    def clean(self):
        if user is None:
            raise forms.ValidationError('Invalid username or password')
        return self.cleaned_data


    