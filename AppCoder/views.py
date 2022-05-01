from django.shortcuts import render
from .models import Curso
from django.http import  HttpResponse


def curso(self):
    curso= Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto =f"Curso : {curso.nombre} comision:{curso.comision}"
    return HttpResponse(texto) 
