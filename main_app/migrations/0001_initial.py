# Generated by Django 4.2.6 on 2023-10-16 18:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('measurements', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('instructions', models.TextField(max_length=250)),
                ('category', models.CharField(choices=[('ordinary drink', 'Ordinary Drink'), ('cocktail', 'Cocktail'), ('shake', 'Shake'), ('other/unknown', 'Other'), ('cocoa', 'Cocoa'), ('shot', 'Shot'), ('coffee/tea', 'Coffee and Tea'), ('homemade liqueur', 'Homemade Liqueur'), ('punch/party drink', 'Party Drink'), ('beer', 'Beer'), ('soft drink', 'Soft Drink')], default='ordinary drink', max_length=100)),
                ('glass', models.CharField(choices=[('highball glass', 'Highball Glass'), ('cocktail glass', 'Cocktail Glass'), ('old-fashioned glass', 'Old-fashioned Glass'), ('whiskey glass', 'Whiskey Glass'), ('collins glass', 'Collins Glass'), ('pousse cafe glass', 'Pousse Cafe Glass'), ('champagne flut', 'Champagne Flute'), ('whiskey sour glass', 'Whiskey Sour Glass'), ('cordial glass', 'Cordial Glass'), ('brandy snifter', 'Brandy Snifter'), ('white wine glass', 'White Wine Glass'), ('nick and nora glass', 'Nick and Nora Glass'), ('hurricane glass', 'Hurrican Glass'), ('coffee mug', 'Coffee Mug'), ('shot glass', 'Shot Glass'), ('jar', 'Jar'), ('irish coffee cup', 'Irish Coffee Cup'), ('punch bowl', 'Punch Bowl'), ('pitcher', 'Pitcher'), ('pint glass', 'Pint Glass'), ('copper mug', 'Copper Mug'), ('wine glass', 'Wine Glass'), ('beer mug', 'Beer Mug'), ('margarita/coupette glass', 'Margarita/Coupette Glass'), ('beer pilsner', 'Beer Pilsner'), ('beer glass', 'Beer Glass'), ('parfait glass', 'Parfait Glass'), ('mason jar', 'Mason Jar'), ('margarita glass', 'Margarita Glass'), ('martini glass', 'Martini Glass'), ('balloon glass', 'Balloon Glass'), ('coupe glass', 'Coupe Glass')], max_length=100)),
            ],
        ),
    ]
