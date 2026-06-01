from rest_framework import serializers
from .models import Categoria, Aviso

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class AvisoSerializer(serializers.ModelSerializer):

    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model = Aviso
        fields = ['id', 'titulo', 'contenido', 'categoria', 'categoria_nombre', 'fecha_creacion']