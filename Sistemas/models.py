from django.db import models
from datetime import datetime
from secrets import token_urlsafe

class Sistemas(models.Model):
    nome = models.CharField(max_length=25, blank=False)
    img = models.CharField(max_length=1, null='1')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = token_urlsafe(16)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nome

class Dados(models.Model):
    sistema = models.ForeignKey(Sistemas, on_delete=models.CASCADE)
    temp = models.CharField(max_length=7)
    voltage = models.CharField(max_length=7)
    current = models.CharField(max_length=7)
    datatime = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self) -> str:
        return self.sistema.nome