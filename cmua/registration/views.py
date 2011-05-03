from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from cmua.registration.models import Register
from cmua.registration.forms import RegistrationForm

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.data['first_name'] + " " + form.data["last_name"]
            return redirect('checkout', name=name)
    else:
        form = RegistrationForm()
    print "form: --------", repr(form)
    return render_to_response("register/index.html",
                              {'form': form},
                              context_instance=RequestContext(request))

def checkout(request, name=""):
    return render_to_response("register/checkout.html", {'name':name},
                              context_instance=RequestContext(request))
