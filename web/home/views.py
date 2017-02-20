# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *


def index_view(request):
    consejo = Dependencia.objects.get(tipo='CD')
    equipo_central = Dependencia.objects.filter(tipo='A')
    equipo_general = Dependencia.objects.filter(tipo='C')
    retiros = Retiro.objects.all()
    ctx = {'consejo': consejo, 'equipo_central': equipo_central, 'equipo_general': equipo_general,
           'retiros': retiros}
    return render_to_response('home/index.html', ctx, context_instance=RequestContext(request))
