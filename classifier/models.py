from django.db import models
import base64

# Create your models here.
class Imagem(models.Model):
    imagem = models.ImageField(upload_to='images')
    print("Teste: " + str(imagem))
    descricao = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.descricao

class Especie(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Inseto(models.Model):
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

class Dado(models.Model):
    inseto = models.ForeignKey(Inseto, on_delete=models.CASCADE)
