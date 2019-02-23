from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms

from django.core.exceptions import ValidationError

@view_function
def process_request(request):
    
    if request.method == 'POST':
        #Populate form with posted data
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/')

    else: # GET
        form = loginForm()

    return request.dmp.render('login.html', {
        'form': form,
    })



class loginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

        
    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError('Invalid username or password')
        return self.cleaned_data
    