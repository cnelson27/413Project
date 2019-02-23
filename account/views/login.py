from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
from django.core.exceptions import ValidationError

@view_function
def process_request(request):
    
    if request.method == 'POST':
        #Populate form with posted data
        form = loginForm(request.POST)
        if form.is_valid():
            login(request, user)
           return 

    context = {
        'form': form,
        'username': username,
        'password': password,
    }

    return request.dmp.render('login.html', context)


    
class loginForm(forms.Form)
    username = forms.CharField(help_text='Enter Username'
    password = forms.CharField(help_text='Enter Password')

    def clean_loginForm(self):
        cleaned_username = self.cleaned_data['username']
        cleaned_password = self.cleaned_data['password']

        user = authenticate(username=cleaned_username, password=cleaned_password)
        if user is not None:
            if user.is_active:
                

        return cleaned_username, cleaned_password, user
    