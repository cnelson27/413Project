from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms
from catalog import models as cmod

@view_function
def process_request(request):
    if request.user.is_authenticated == True:
        theCart = request.user.get_shopping_cart()
        theCart.recalculate()
        cartItems = cmod.SaleItem.objects.filter(sale=theCart, status='A')
    else:
        return HttpResponseRedirect('/account/login/')

    return request.dmp.render('cart.html', { 
        'cart': theCart,
        'cartItems': cartItems,
    })

@view_function
def remove(request, saleItem):
    cartItem = cmod.SaleItem.objects.get(id=saleItem)
    cartItem.status = 'D'
    cartItem.save()
    cartItem.sale.recalculate()
    cartItem.sale.save()
    return HttpResponseRedirect('/catalog/cart/')
