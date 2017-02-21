# -*- coding: utf-8 -*-
from django.db import models
from fontawesome.fields import IconField


class Dirigente(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return "%s" % self.nombre


class Dependencia(models.Model):
    TIPO_DEPENDENCIA = (
        ('CD', 'Consejo Directivo'),
        ('A', 'Área'),
        ('C', 'Comisión')
    )
    tipo = models.CharField(max_length=20, choices=TIPO_DEPENDENCIA)
    icono = IconField()
    coordinador = models.ManyToManyField('Dirigente')
    miembro = models.ManyToManyField('Dirigente', blank=True, related_name='miembro')
    nombre = models.CharField(max_length=50)
    objetivo_general = models.TextField()
    objetivo_especifico = models.TextField(blank=True)

    def __unicode__(self):
        return "%s" % self.nombre



class Retiro(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    requisito = models.ForeignKey('RetiroRequisito')
    casa = models.ForeignKey('RetiroCasa')
    fecha_inscripcion = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return "%s -> Inicio: %s %s" % (self.nombre, self.fecha_inicio.strftime("%d/%m/%y"), self.casa)


class RetiroRequisito(models.Model):
    nombre = models.CharField(max_length=100)
    requisito = models.TextField()

    def __unicode__(self):
        return self.nombre


class RetiroCasa(models.Model):
    nombre = models.CharField(max_length=100)
    informacion = models.TextField()
    croqui = models.FileField(blank=True)

    def __unicode__(self):
        return self.nombre
