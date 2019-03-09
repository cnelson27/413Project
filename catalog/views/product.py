from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.core.exceptions import ValidationError
from catalog import models as cmod

@view_function
def process_request(request):
    
    return request.dmp.render('index.html')

# @view_function
# def tile(request, cmod.Product):


#     return request.dmp.render('index.html')
# @view_function
# def process_request(request, product:cmod.Product)
#     return request.dmp.render('product.html')


    