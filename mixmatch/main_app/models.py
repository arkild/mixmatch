from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Drinks(models.Model):
    name = models.CharField(max_length=100)
    # Found a Field for listing items.
    # https://docs.djangoproject.com/en/4.2/ref/contrib/postgres/fields/
    ingredients = ArrayField(models.Charfield(max_length=100))
    measurements = ArrayField(models.Charfield(max_length=100))
    instructions = models.Textfield(max_length=250)
    