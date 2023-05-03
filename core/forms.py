from django import forms
from .models import Curso,Colegio


class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields= '__all__'

class ColegioForm(forms.ModelForm):
    class Meta:
        model=Colegio
        fields= '__all__'