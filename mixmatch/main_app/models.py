from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Drinks(models.Model):
    name = models.CharField(max_length=100)
    ingredients = ArrayField(models.Charfield(max_length=100))