from django.db import models

class Thing(models.Model):
    name = models.CharField(blank=False, max_length=30, unique=True)
    description = models.CharField(blank=True, max_length=120, unique=False)
    quantity = models.PositiveIntegerField(unique= False, max_length=100, blank=False)

