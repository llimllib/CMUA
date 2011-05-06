from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django.shortcuts import render_to_response, redirect

from urllib import quote

from cmua.registration.models import Register
from cmua.registration.forms import RegistrationForm

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.data['first_name'] + " " + form.data["last_name"]

            send_mail("Thanks for registering with CMUA",
"""%s,

Thank you for registering for a CMUA 2011 league.

If you haven't yet paid for the league, you can do so by visiting http://md-ultimate.org/register/checkout.html/%s and clicking the google payment button or following the instructions for mailing in a check.

Have a great season!""" % (name, quote(name)),
                      'cmua@md-ultimate.org',
                      [form.data['email_address']],
                      fail_silently=True)
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
