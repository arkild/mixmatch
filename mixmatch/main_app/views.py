from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Drink
from .forms import ReviewForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Drink index route
def drinks_index(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/index.html', {'drinks': drinks})

# Drink detail view

def drink_detail(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    return render(request, 'drinks/details.html', {'drink': drink})

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

# REVIEW VIEWS

# add a review
# def add_review(request, drink_id):
#     form = ReviewForm(request.POST)
#     # Validate the form
#     if form.is_valid():
#         # Don't save the form to the database until it has the ID assigned
#         new_review = form.save(commit=False)
#         new_review.drink_id = drink_id
#         new_review.save()
#     return redirect('detail', drink_id = drink_id)
