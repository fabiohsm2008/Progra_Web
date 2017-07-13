# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime 
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Pregunta(models.Model):
    question_text = models.CharField(max_length=800)
    pub_date = models.DateTimeField('date published')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()

class Respuesta(models.Model):
    question = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    respuesta = models.TextField()
    best = models.BooleanField(default=False)
