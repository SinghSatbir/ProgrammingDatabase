from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from pdbapp.models import Item


def index(request):
    template = loader.get_template('index.html')
    context = {
        'items' : Item.objects.all()
    }
    return HttpResponse(template.render(context,request))