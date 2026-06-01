from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VistaCategoria, VistaAviso

# El router crea automáticamente las rutas de la API
router = DefaultRouter()
router.register(r'categorias', VistaCategoria)
router.register(r'avisos', VistaAviso)

urlpatterns = [
    path('', include(router.urls)),
]