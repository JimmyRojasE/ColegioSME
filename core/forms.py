from django import forms
from .models import Curso,Colegio, Direccion, GrupoFamiliar, CursoRepetido


class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields= '__all__'

class ColegioForm(forms.ModelForm):
    class Meta:
        model=Colegio
        fields= '__all__'

class DireccionForm(forms.ModelForm):
    class Meta:
        model=Direccion
        fields= '__all__'

class GrupoFamiliarForm(forms.ModelForm):
    class Meta:
        model=GrupoFamiliar
        fields=('id_gr_fam','nombre','edad','parentesco')       

class CursoRepetidoForm(forms.ModelForm):
    class Meta:
        model=CursoRepetido
        fields=('__all__')    