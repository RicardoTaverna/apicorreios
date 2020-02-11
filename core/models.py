from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    cep = models.CharField(max_length=20)
    rua = models.CharField(max_length=400)
    complemento = models.CharField(max_length=400)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=10)

    def __str__(self):
        return self.nome