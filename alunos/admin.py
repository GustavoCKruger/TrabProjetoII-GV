from django.contrib import admin

from django.contrib import admin
from .models import Estado, Cidade, Aluno, Clientes, Pedidos, Itens

admin.site.register(Estado)

admin.site.register(Cidade)

admin.site.register(Aluno)

admin.site.register(Clientes)

admin.site.register(Pedidos)

admin.site.register(Itens)