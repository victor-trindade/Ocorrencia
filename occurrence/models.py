from django.db import models
from store.models import Store


class Occurrence(models.Model):
    date = models.DateField()
    photo = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    obs = models.TextField(max_length=280)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.store.name