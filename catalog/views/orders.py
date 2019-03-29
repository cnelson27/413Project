from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms
from catalog import models as cmod

@view_function
def process_request(request):
    if request.user.is_authenticated == True:
        sales = cmod.Sale.objects.filter(user=request.user, purchased__isnull = False).order_by('purchased')
    else:
        return HttpResponseRedirect('/account/login/')

    return request.dmp.render('orders.html', { 
        'sales' : sales,
    })