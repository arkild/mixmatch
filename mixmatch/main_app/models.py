from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
# Create your models here.

CATEGORIES = (
   ('ordinary drink', 'Ordinary Drink'),
   ('cocktail', 'Cocktail'),
   ('shake', 'Shake'),
   ('other/unknown', 'Other'),
   ('cocoa', 'Cocoa'),
   ('shot', 'Shot'),
   ('coffee/tea', 'Coffee and Tea'),
   ('homemade liqueur', 'Homemade Liqueur'),
   ('punch/party drink', 'Party Drink'),
   ('beer', 'Beer'),
   ('soft drink', 'Soft Drink'),
)

class Drink(models.Model):
    name = models.CharField(max_length=100)
    # Found a Field for listing items.
    # https://docs.djangoproject.com/en/4.2/ref/contrib/postgres/fields/
    ingredients = ArrayField(models.Charfield(max_length=100))
    measurements = ArrayField(models.Charfield(max_length=100))
    instructions = models.Textfield(max_length=250)
    category = models.CharField(max_length=100, choices=CATEGORIES, default=CATEGORIES[0][0])
    
    