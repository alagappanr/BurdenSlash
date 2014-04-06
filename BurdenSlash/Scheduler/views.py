from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    #home page render
    return  render_to_response('home.html', context_instance=RequestContext(request));



