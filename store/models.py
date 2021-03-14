from django.db import models


# Create your models here.

class Store(models.Model):
    sf_id = models.CharField(max_length=18, blank=True, null=True)
    name = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.name