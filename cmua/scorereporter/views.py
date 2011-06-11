from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from cmua.scorereporter.forms import ScoreReportForm
from cmua.scorereporter.models import Team

def index(request):
    if request.method == 'POST':
        form = ScoreReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ScoreReportForm()
    print "form: --------", repr(form)
    return render_to_response("scorereporter/index.html",
                              {'form': form},
                              context_instance=RequestContext(request))

def standings(request):
    standings = sorted((t.standings for t in Team.objects.all()), reverse=True)

    return render_to_response("scorereporter/standings.html",
                              {'standings': standings},
                              context_instance=RequestContext(request))
