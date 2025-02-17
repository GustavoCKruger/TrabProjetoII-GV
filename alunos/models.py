from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} - {self.sigla}'
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} - {self.estado.sigla}'

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome 

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    


class Pedidos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    data = models.DateField()
    valor = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cliente.nome}'

class Itens(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    produto = models.CharField(max_length=100)
    quant = models.CharField(max_length=100)
    precouni = models.CharField(max_length=100)

    def __str__(self):
        return self.produto


    