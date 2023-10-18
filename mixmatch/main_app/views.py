from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Drink, Review
from .forms import ReviewForm, DrinkForm

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
    reviews = Review.objects.all()
    review_form = ReviewForm()
    return render(request, 'drinks/details.html', {'drink': drink,"review_form": review_form, "reviews": reviews})

# Create Drink view
# class DrinkCreate(LoginRequiredMixin, CreateView):
class DrinkCreate(CreateView):
    model = Drink
    form_class = DrinkForm # as of right now, I don't know what fields may need to be worked on - Winston can edit this where appropriate
    # success_url = '/drinks'
    #Checking when form is valid
    def form_valid(self,form):
        # Assign to the logged in user
        form.instance.user = self.request.user # form.instance is the drink
        #This then does what the CreateView normally does
        return super().form_valid(form)

# Update Drink view
# class DrinkUpdate(LoginRequiredMixin, UpdateView):
class DrinkUpdate(UpdateView):
    model = Drink
    fields = '__all__' #Winston can change the fields to what he wants edited
    # success_url = '/drinks'
    
# Delete Drink view 
# class DrinkDelete(LoginRequiredMixin, DeleteView):
class DrinkDelete(DeleteView):
    model = Drink
    success_url = '/drinks'

# REVIEW VIEWS

# Add a review
# @login_required
def add_review(request, drink_id):
    form = ReviewForm(request.POST)
    # Validate the form
    if form.is_valid():
        # Don't save the form to the database until it has the ID assigned
        new_review = form.save(commit=False)
        new_review.drink_id = drink_id
        new_review.save()
    return redirect('details', drink_id=drink_id)
    
# Edit a Review - We're using a similar form to drink edits for this
# class ReviewUpdate(LoginRequiredMixin, UpdateView):
class ReviewUpdate(UpdateView):
    model = Review
    fields = '__all__' # Edit this line with what fields need to be updated

# Delete Review
# class ReviewDelete(LoginRequiredMixin, DeleteView):
class ReviewDelete(DeleteView):
    model = Review
    success_url = '/drinks'

def signup(request):
    error_message = ''
    if request.method == 'post':
        #This will use the data from the browser to create a user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #Add the user to the database
            user = form.save()
            # Log the user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# This will render a page that refers only to the user's created drinks
# @login_required
# def user_drinks(request):
#     drinks = Drink.objects.filter(user=request.user)
#     return render(request, 'user/index.html', { 'drinks': drinks})