from django import forms
from .models import Curso, Direccion, GrupoFamiliar, CursoRepetido, Usuario


class CursoForm(forms.ModelForm):
    id_curso=forms.CharField(label=False,required=True, widget=forms.TextInput(attrs={'class':'oculto'}))
    class Meta:
        model=Curso
        fields= ['id_lista_curso' , 'id_tipo_curso' , 'id_jornada' , 'profesor_jefe']
   

    
        
# class ColegioForm(forms.ModelForm):
#     class Meta:
#         model=Colegio
#         fields= '__all__'

class DireccionForm(forms.ModelForm):
    class Meta:
        model=Direccion
        fields= '__all__'

class GrupoFamiliarForm(forms.ModelForm):
    class Meta:
        model=GrupoFamiliar
        fields=('__all__')

# class CursoRepetidoForm(forms.ModelForm):
#     class Meta:
#         model=CursoRepetido
#         fields=('id_curso_repetido','id_lista_curso','anno_repitencia','id_matricula')    

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=('__all__')    