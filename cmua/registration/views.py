from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from registration.models import Register
from registration.forms import RegistrationForm

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #TODO: process the form
            return HttpResponseRedirect('/register/thanks.html')
    else:
        form = RegistrationForm()
    print "form: --------", repr(form)
    return render_to_response("register/index.html",
                              {'form': form},
                              context_instance=RequestContext(request))
