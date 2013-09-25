import json, logging
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User

from neefty.models import Dimension, ListItem
from neefty.forms import DimensionForm, ListItemForm

logger = logging.getLogger(__name__)

def home(request):
    context = {
        'user' : request.user.username
        }
    return render_to_response("main/home.html",context, context_instance=RequestContext(request))
                
@login_required()
def addDimension(request):
    data = {'status' : 'ok'}
    try:
        if request.method == 'POST':
            d = Dimension()
            d.name = request.POST.get('name')
            d.user = request.user
            d.save()
            data['message' : '%s dimension Added' % d.name]
        else:
            data['status'] = 'error'
            data['message'] = 'Operation not allowed'
    except Exception as e:
        logger.exception(e)
        data['status'] = 'error'
        data['message'] = str(e)
                    
    return HttpResponse(json.dumps(data), 'application/json')   
                
def urlencode(request):
    context = {}
    return render_to_response("webtools/urlencode.html",context, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('/')
        # Redirect to a success page.