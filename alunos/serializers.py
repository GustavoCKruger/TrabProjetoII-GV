from rest_framework.serializers import ModelSerializer
from .models import Estado, Cidade, Aluno, Clientes, Pedidos, Itens

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class PedidosSerializer(ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'


class ItensSerializer(ModelSerializer):
    class Meta:
        model = Itens
        fields = '__all__'