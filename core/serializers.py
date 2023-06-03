from .models import *
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Region
        fields = '__all__'