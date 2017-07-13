# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import time 
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Pregunta(models.Model):
    question_text = models.CharField(max_length=800)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Respuesta(models.Model):
    question = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    respuesta = models.TextField()
    best = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)