from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms
from catalog import models as cmod
from django.core.exceptions import ValidationError


@view_function
def process_request(request):
    # productnum = 0
    # imgnum = 0
    # for i in range(6):
    #     prod = cmod.Product()
    #     prod.name = PRODUCTS[productnum]
    #     prod.status = 'A'
    #     prod.description = 'The best ' + PRODUCTS[productnum] + ' on the market!'
    #     prod.price = 800.85
    #     prod.category = cmod.Category.objects.get(id = 3)
    #     prod.save()
    #     for j in range(2):
    #         prodimg = cmod.ProductImage()
    #         prodimg.filename = IMAGES[imgnum]
    #         prodimg.product = cmod.Product.objects.get(name=PRODUCTS[productnum])
    #         imgnum+=1
    #         prodimg.save()
    #     productnum+=1

    return request.dmp.render('index.html')


    