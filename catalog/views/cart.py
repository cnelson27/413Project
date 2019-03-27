from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms
from catalog import models as cmod

@view_function
def process_request(request):

    return request.dmp.render('cart.html', {  
    })
