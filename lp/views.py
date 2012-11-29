# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.core import serializers

from litpress import settings
from lp.models import usermeta


def IndexView(request):
    template_name = 'index.html'
    dict = {}
    if settings.USE_THEME:
        theme_name = usermeta.objects.get(meta_key = "theme").meta_value
        theme_dir = settings.BASE_DIR + "/../content/themes/"+theme_name
    
    t = TemplateResponse(request, theme_dir + '/index.html')
    t.render()
    return t

def load_template(template_name):
    return render_to_response(template_name)


