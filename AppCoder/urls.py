from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('cursos/', cursos),
    path('entregables/', entregables),

]
