from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms
import math
from catalog import models as cmod
from django.core.exceptions import ValidationError

ITEMS_PER_PAGE = 8

@view_function
def process_request(request, category:cmod.Category=None, page:int=1):
    products = cmod.Product.objects.filter(status="A")
    if category is not None:
        products = products.filter(category=category)
    products = products[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]

    return request.dmp.render('index.html', {
        'category' : category,
        'products' : products,
        'page' : page,
        'numpages' : math.ceil(products.count() / ITEMS_PER_PAGE),   
    })


    