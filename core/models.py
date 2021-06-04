from django.db import models

# Create your models here.


class Posts(models.Model):
    titulo = models.CharField('titulo', max_length=60)
    subtitulo = models.CharField('subtitulo', max_length=120)
    texto = models.TextField('texto', max_length=1000)

    def __str__(self):
        return self.titulo
