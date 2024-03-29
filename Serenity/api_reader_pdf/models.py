from django.db import models
from chatbot.models import Usuario

class Embedding(models.Model):
    contenido_texto = models.JSONField()
    embeddings = models.JSONField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='embeddings', null=True)

    def __str__(self):
        return self.nombre_archivo
