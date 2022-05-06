from django import forms

class CursoFormulario(forms.Form):
    #Especificamos los campos de formulario
    nombre = forms.CharField(max_length=50)
    comision= forms.IntegerField()



