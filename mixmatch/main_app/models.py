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

GLASSES = (
    ('highball glass', 'Highball Glass'),
    ('cocktail glass', 'Cocktail Glass'),
    ('old-fashioned glass', 'Old-fashioned Glass'),
    ('whiskey glass', 'Whiskey Glass'),
    ('collins glass', 'Collins Glass'),
    ('pousse cafe glass', 'Pousse Cafe Glass'),
    ('champagne flut', 'Champagne Flute'),
    ('whiskey sour glass', 'Whiskey Sour Glass'),
    ('cordial glass', 'Cordial Glass'),
    ('brandy snifter', 'Brandy Snifter'),
    ('white wine glass', 'White Wine Glass'), 
    ('nick and nora glass', 'Nick and Nora Glass'),
    ('hurricane glass', 'Hurrican Glass'),
    ('coffee mug', 'Coffee Mug'),
    ('shot glass', 'Shot Glass'),
    ('jar', 'Jar'),
    ('irish coffee cup', 'Irish Coffee Cup'),
    ('punch bowl', 'Punch Bowl'),
    ('pitcher', 'Pitcher'),
    ('pint glass', 'Pint Glass'),
    ('copper mug', 'Copper Mug'),
    ('wine glass', 'Wine Glass'),
    ('beer mug', 'Beer Mug'),
    ('margarita/coupette glass', 'Margarita/Coupette Glass'),
    ('beer pilsner', 'Beer Pilsner'),
    ('beer glass', 'Beer Glass'),
    ('parfait glass', 'Parfait Glass'),
    ('mason jar', 'Mason Jar'),
    ('margarita glass', 'Margarita Glass'),
    ('martini glass', 'Martini Glass'),
    ('balloon glass', 'Balloon Glass'),
    ('coupe glass', 'Coupe Glass')
)

class Drink(models.Model):
    name = models.CharField(max_length=100)
    # Found a Field for listing items.
    # https://docs.djangoproject.com/en/4.2/ref/contrib/postgres/fields/
    ingredients = ArrayField(models.Charfield(max_length=100))
    measurements = ArrayField(models.Charfield(max_length=100))
    instructions = models.Textfield(max_length=250)
    category = models.CharField(max_length=100, choices=CATEGORIES, default=CATEGORIES[0][0])
    glass = models.CharField(max_length=100, choices=GLASSES)
    # reviews =  models.ForeignKey(Review, on_delete=models.CASCADE)
    # image = 
    def __str__(self):
        return self.name
    
    
# class Review(models.Model):
    



# class User(models.Model):
    
    
    
    
    