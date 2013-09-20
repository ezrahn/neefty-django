from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.shortcuts import redirect


def home(request):
    context = {
        'user' : request.user.username
        }
    return render_to_response("webtools/home.html",context, context_instance=RequestContext(request))
                
def urlencode(request):
    context = {}
    return render_to_response("webtools/urlencode.html",context, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('/')
        # Redirect to a success page.