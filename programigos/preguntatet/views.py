# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import time 
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import *
from django.contrib.auth.models import User
from .models import Pregunta, Respuesta
import json

def Preguntation(request):
	template = loader.get_template('preguntar.html')
	context = {}
	titulo = request.POST.get('Pregunta_Titulo','')
	descripcion_pregunta = request.POST.get('Pregunta_Usuario','')
	question = Pregunta(question_text = titulo, usuario = User.objects.get(pk=request.session['idUser']), descripcion = descripcion_pregunta)
	question.save()
	return HttpResponse(template.render(context,request))
# Create your views here.
