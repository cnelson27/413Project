from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.core.exceptions import ValidationError
from catalog import models as cmod

@view_function
def process_request(request, product):
    
    return request.dmp.render('product.html', {
        'product' : product,
    })


@view_function
def tile(request, product):
    theproduct = cmod.Product.objects.get(id=product)
    print(theproduct)
    print(theproduct)
    print(theproduct)
    print(theproduct)
    print(product)
    print(product)
    print(product)
    print(product)
    print(product)
    return request.dmp.render('product.tile.html', {
        'product' : theproduct,
    })


    