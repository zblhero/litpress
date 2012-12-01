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
from lp.models import posts as lp_posts
from lp.models import options as lp_options


def IndexView(request):
    template_name = 'index.html'
    dict = {}
    
    posts = lp_posts.objects.all()
    options = lp_options.objects.all()
    dict['posts'] = posts
    
    t = TemplateResponse(request, 'index.html', dict)
    t.render()
    return t

def load_template(template_name):
    return render_to_response(template_name)


