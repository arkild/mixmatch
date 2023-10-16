from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # __all__ is a placeholder; fill it with what it needs to be after.