from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Pergunta(models.Model):
    txt_pergunta = models.CharField(max_length=200)
    dt_pub = models.DateTimeField('Data da Publicacao')

    def __str__(self):
        return self.txt_pergunta

    def pub_recente(self):
        return self.dt_pub >= timezone.now() - datetime.timedelta(days=-1)

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    txt_resposta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.txt_resposta
