from rest_framework import viewsets, permissions
from .models import Aviso, Categoria
from .serializers import AvisoSerializer, CategoriaSerializer

class PermisoAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class VistaCategoria(viewsets.ModelViewSet):  # <-- ¡Aquí está el nombre exacto!
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [PermisoAdmin]

class VistaAviso(viewsets.ModelViewSet):      # <-- ¡Y aquí está el otro!
    queryset = Aviso.objects.all().order_by('-fecha_creacion')
    serializer_class = AvisoSerializer
    permission_classes = [PermisoAdmin]
    
    def get_queryset(self):
        avisos = super().get_queryset()
        categoria_buscada = self.request.query_params.get('categoria')
        if categoria_buscada:
            avisos = avisos.filter(categoria_id=categoria_buscada)
        return avisos