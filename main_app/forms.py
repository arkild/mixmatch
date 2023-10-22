from django.forms import ModelForm
from django import forms
from .models import Review
from .models import Drink

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'description']

class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'ingredients', 'measurements', 'instructions', 'category', 'glass'] 

# Added for for search function
class SearchForm(forms.Form):
    query = forms.CharField()