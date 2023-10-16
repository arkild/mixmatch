from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Drink

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Drink index route
# def drinks_index(request):
    # return render(request, 'drinks/index.html', {'drinks': drinks})

# Drink detail view

# def drink_detail(request, drink_id):
#     drink = Drink.objects.get(id=drink_id)
#     return render(request, 'drinks/details.html', {'drink': drink})

# Create Drink view

# class DrinkCreate(CreateView):
#     model = Drink
#     fields = '__all__' #as of right now, I don't know what fields may need to be worked on - Winston can edit this where appropriate

# Update Drink view

# class DrinkUpdate(UpdateView):
#     model = Drink
#     fields = '__all__' #Winston can change the fields to what he wants edited

# Delete Drink view 

# class DrinkDelete(DeleteView):
#     model = Drink
#     success_url = '/drinks'
