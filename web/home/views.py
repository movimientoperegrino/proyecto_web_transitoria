# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *


def index_view(request):
    consejo = Dependencia.objects.get(tipo='CD')
    equipo_central = Dependencia.objects.filter(tipo='A').order_by('nombre')
    equipo_general = Dependencia.objects.filter(tipo='C').order_by('nombre')
    retiros = Retiro.objects.all().order_by('fecha_inicio')
    casas_retiro = RetiroCasa.all().order_by('nombre')
    ctx = {'consejo': consejo, 'equipo_central': equipo_central, 'equipo_general': equipo_general,
           'retiros': retiros, 'casas': casas_retiro}
    return render_to_response('home/index.html', ctx, context_instance=RequestContext(request))
