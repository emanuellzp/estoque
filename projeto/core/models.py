from django.db import models

# Create your models here.

# Atualizar a data somente quando criar algo...

class TimeStampedModel(models.Model):
    created = models.DateTimeFIeld(
        'Criado em: ',
        auto_now_add=True,
        auto_now=False
    )

    # Atualiza a data e a hora quando estiver modificando algum registro...
    modified = models.DateTimeField(
        'Modificado em: ',
        auto_now_add=False,
        auto_now=True
    )

    # Significa que irei usar como herança em outros models...
    class Meta:
        abstract = True