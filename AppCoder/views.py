from django.shortcuts import render
from .models import Curso
from django.http import  HttpResponse
from AppCoder.forms import CursoFormulario


def curso(self):
    curso= Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto =f"Curso : {curso.nombre} comision:{curso.comision}"
    return HttpResponse(texto) 

def inicio(request):
    return render(request,'AppCoder/inicio.html')

def profesores(request):
    return render(request,'AppCoder/profesores.html')

def estudiantes(request):
    return render(request,'AppCoder/estudiantes.html')



def entregables(request):
    return render(request,'AppCoder/entregables.html')



#-------------------------------------------------------------------------
def cursos(request):

    #-------SI entra por Post cuando viene un formulario cargado--------
    if request.method =='POST':

        #Crea una variable donde llama a la clase CrearFormulario con los datos que viene por request
        miFormulario = CursoFormulario(request.POST)
        
        #Pregunta que este todo ok o sea que sean los datos compatibles
        if miFormulario.is_valid():
            #Crea una variable  informacion y saca la basura
            informacion = miFormulario.cleaned_data
            #Asigna esos dato limpiados a la creacion del cursos con esos parametros
            curso = Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request,'AppCoder/inicio.html')
    else:
        miFormulario= CursoFormulario()
    return render(request, 'AppCoder/cursos.html' , {'formulario': miFormulario})
#------------------------------------------------------------------------------------



def busquedaComision(request):
    return render (request, 'AppCoder/busquedaComision.html')


def buscar(request):
    if request.GET['comision']:
        comision=request.GET['comision']
        cursos= Curso.objects.filter(comision=comision)

        return render(request,'AppCoder/resultadosBusqueda.html', {'cursos': cursos, 'comision': comision})
    else:
        repuesta= "No se ingreso ninguna comision"
        return render(request,'AppCoder/resultadosBusqueda.html', {'repuesta': repuesta}) 
        

    



