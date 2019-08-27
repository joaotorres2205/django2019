from django.db import models

class Aluno(models.Model) :
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    email = models.CharField(max_length=50)

    def __set__(self):
        return self.nome