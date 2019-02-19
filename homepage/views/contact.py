from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    # did the user submit?
    if request.method == "POST":
        # check all the variables
        # we assume the user does it wrong
        print(request.POST["yourname"])
        print(request.POST["youremail"])
        # if user did do it right:
        # do the work (reset password, create account, finalize the sale)
        #return HttpResponseRedirect(homepage/contact/)
    context = {
    }
    return request.dmp.render('contact.html', context)