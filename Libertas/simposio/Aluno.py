from django.db import models

class Aluno(models.Model) :
    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 15)
    usuario = models.CharField(max_length = 50)
    senha = models.CharField(max_length = 20)
    
    def __set__(self):
        return self.nome