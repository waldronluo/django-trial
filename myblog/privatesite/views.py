import os
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, Http404
from django.utils._os import safe_join
from django.conf import settings
from privatesite.models import p_block
from privatesite.models import p_list_item

def index(request):
    t = loader.get_template("base.html")
    blocks = p_block.objects.all()
    items = p_list_item.objects.all()
    c = Context({'blocks':blocks,
                 'items':items,
                 })
    return HttpResponse(t.render(c))

def staticFileAccess(request):
    try:
        file_path = safe_join(settings.BASE_DIR,
                settings.BASE_DIR + request.get_full_path())
    except ValueError:
        raise Http404('404 Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('404 Not Found')

    with open(file_path, 'r') as f:
        content = f.read()

    response = HttpResponse()
    response.write(content)
    return response

# Create your views here.
