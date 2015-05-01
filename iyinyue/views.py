__author__ = 'Administrator'
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', RequestContext(request, {}))


def genres(request):
    return render_to_response('music/genres.html', RequestContext(request, {}))


def listen(request):
    return render_to_response('listen.html', RequestContext(request, {}))


def not_found(request):
    return render_to_response('404.html', RequestContext(request, {}))


# TODO delete
def detail(request):
    return render_to_response('music/detail.html', RequestContext(request, {}))
