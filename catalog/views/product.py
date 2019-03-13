from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.core.exceptions import ValidationError
from catalog import models as cmod

@view_function
def process_request(request, product):
    theproduct = cmod.Product.objects.get(id=product)
    thumbnails = theproduct.image_urls()
    featured = thumbnails[0]
    del thumbnails[0]
    return request.dmp.render('product.html', {
        'product' : theproduct,
        'thumbnails' : thumbnails,
        'featured' : featured,
    })


@view_function
def tile(request, product):
    theproduct = cmod.Product.objects.get(id=product)
    return request.dmp.render('product.tile.html', {
        'product' : theproduct,
    })


    