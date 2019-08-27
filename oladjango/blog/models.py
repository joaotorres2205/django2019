from django.db import models

# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    resumo = models.TextField()

    def __str__(self):
        return self.autor

class Produto(models.Model) :
    descricao = models.TextField()
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits = 7, decimal_places = 2)
    cod_barras = models.CharField(max_length=100)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao

#criar uma class de fornecedor contendo nome, cnpj, endereco

class Fornecedor(models.Model) :
    nome = models.CharField(max_length=60)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome


#criar cadastro de cidade vinculando ao fornecedor

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
