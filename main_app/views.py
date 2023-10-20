from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# Make sure you import Drink
from .models import Drink, Review, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm, DrinkForm
# INSTALL This: pip3 install boto3
import boto3
import uuid
import os


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
class DrinkCreate(LoginRequiredMixin, CreateView):
# When commenting in the line above, DELETE THIS LINE BELOW
# class DrinkCreate(CreateView):
    model = Drink
    fields = ['name', 'ingredients', 'measurements', 'instructions', 'category', 'glass'] 
    # as of right now, I don't know what fields may need to be worked on - Winston can edit this where appropriate
    success_url = '/drinks'

# Update Drink view
class DrinkUpdate(LoginRequiredMixin, UpdateView):
# When commenting in the line above, DELETE THIS LINE BELOW
# class DrinkUpdate(UpdateView):
    model = Drink
    fields = ['name', 'ingredients', 'measurements', 'instructions', 'category', 'glass']  #Winston can change the fields to what he wants edited
    # success_url = '/drinks'
    
# Delete Drink view 
class DrinkDelete(LoginRequiredMixin, DeleteView):
# When commenting in the line above, DELETE THIS LINE BELOW
# class DrinkDelete(DeleteView):
    model = Drink
    success_url = '/drinks'

# REVIEW VIEWS

# Add a review
@login_required
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
class ReviewUpdate(LoginRequiredMixin, UpdateView):
# When commenting in the line above, DELETE THIS LINE BELOW
# class ReviewUpdate(UpdateView):
    model = Review
    fields = '__all__' # Edit this line with what fields need to be updated

# Delete Review
class ReviewDelete(LoginRequiredMixin, DeleteView):
# When commenting in the line above, DELETE THIS LINE BELOW
# class ReviewDelete(DeleteView):
    model = Review
    success_url = '/drinks'



    #Add photo view 
    #This would normally be a login required situation but you can only add photos on the Create Drink page
def add_photo(request, drink_id):
    #photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        #need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # Just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            #build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to drink_id or drink (if you have a drink object)
            Photo.objects.create(url=url, drink_id=drink_id)
        except Exception as e:
            print('An error occured uploading file to S3')
            print(e)
    return redirect('details', drink_id=drink_id)
            

def signup(request):
    error_message = ''
    if request.method == 'POST':
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
@login_required
def user_drinks(request):
    drinks = Drink.objects.filter(user=request.user)
    return render(request, 'user/index.html', { 'drinks': drinks })

# class SearchView(ListView):
#     # Pulls from the drink model
#     model = Drink
#     template_name = 'search.html'
#     context_object_name = 'all_search_results'

#     def get_queryset(self):
#         result = super(SearchView, self).get_queryset()
#         query = self.request.GET.get('search')
#         if query: # If there's something in there worth filtering
#             #filter it in here
#             postresult = Drink.objects.filter(name__contains=query) # I changed this from title to name from the stackoverflow article because I believe it's calling for the field, not specific syntax.
#             result = postresult
#         else:
#             result = None
#         return result
