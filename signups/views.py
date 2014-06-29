from django.shortcuts import render, render_to_response, RequestContext

from .forms import SingUpForm


def home(request):

    form = SingUpForm()

    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))
