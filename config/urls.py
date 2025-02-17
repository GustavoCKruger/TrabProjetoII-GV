"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import EstadoViewSet, CidadeViewSet, AlunoViewSet, ClientesViewSet, PedidosViewSet, ItensViewSet

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'cidade', CidadeViewSet)
router.register(r'aluno', AlunoViewSet)
router.register(r'clientes', ClientesViewSet)
router.register(r'pedidos', PedidosViewSet)
router.register(r'itens', ItensViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]