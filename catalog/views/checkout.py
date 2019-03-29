from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.core.exceptions import ValidationError
from catalog import models as cmod
from django import forms
from account import models as amod

@view_function
def process_request(request):
    if request.user.is_authenticated == True:
        cart = request.user.get_shopping_cart()
        cart.recalculate()

    if request.method == "POST":
        form = addressForm(request.POST)
        if request.user.is_authenticated == False:
            return HttpResponseRedirect('/account/login/')

        cart = request.user.get_shopping_cart()
        form.sale = cart
        if form.is_valid():
            return HttpResponseRedirect('/catalog/receipt/' + str(cart.id))   
    else:
        form = addressForm()

    return request.dmp.render('checkout.html', {
        'form' : form,
        'cart' : cart,
    })

class addressForm(forms.Form):
    address = forms.CharField(label="Address")
    city = forms.CharField(label="City")
    state = forms.CharField(label="State")
    zip = forms.CharField(label="Zipcode")
    stripeToken = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        if not cmod.SaleItem.objects.filter(sale=self.sale, status='A').exists():
            raise forms.ValidationError('No Items in Cart')
        try:
            self.sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))
        return self.cleaned_data


    