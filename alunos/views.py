from rest_framework.viewsets import ModelViewSet
from .models import Estado, Cidade, Aluno, Clientes, Pedidos, Itens
from .serializers import EstadoSerializer, CidadeSerializer, AlunoSerializer, ClientesSerializer, PedidosSerializer, ItensSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ClientesViewSet(ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class PedidosViewSet(ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

class ItensViewSet(ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer


