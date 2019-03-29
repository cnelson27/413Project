from django.contrib.auth import authenticate, login
from django_mako_plus import view_function, jscontext
from django.http import HttpResponseRedirect
from django import forms
from catalog import models as cmod

@view_function
def process_request(request, Sale):
    if request.user.is_authenticated == True:
        sale = cmod.Sale.objects.get(id = Sale)
        if sale.purchased == False:
            return HttpResponseRedirect('/catalog/cart/')
        saleItems = cmod.SaleItem.objects.filter(sale=sale, status='A')

        return request.dmp.render('receipt.html', {
            'sale' : sale,
            'saleItems' : saleItems,
        })
    else:
        return HttpResponseRedirect('/account/login/')