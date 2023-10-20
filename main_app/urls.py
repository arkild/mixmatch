# boilerplate
from django.urls import path
from . import views

# The URLS that are not tested and working are commented out.
# When they work, we will comment them back in and confirm stability.
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    path('drinks/', views.drinks_index, name='index'),
    path('drinks/<int:drink_id>/', views.drink_detail, name='details'),
    path('drinks/create/', views.DrinkCreate.as_view(), name='drinks_create'),
    path('drinks/<int:pk>/update/', views.DrinkUpdate.as_view(), name='drinks_update'),
    path('drinks/<int:pk>/delete/', views.DrinkDelete.as_view(), name='drinks_delete'),
    
    # These review URLs are spitballed - they may need to be adjusted accordingly with how we want our pages to format.
    # Right now, updating and deleting reviews will call for a separate page, and adding reviews can be done on the same page as the drink, but if we want this to change, we have to change these accordingly. 
    path('drinks/<int:drink_id>/add_review/', views.add_review, name='add_review'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name="review_update"),
    path('drinks/<int:pk>/delete/', views.ReviewDelete.as_view(), name="review_delete"),
    # Photo add path
    path('drinks/<int:drink_id>/add_photo/', views.add_photo, name='add_photo'),
    # This path below is specifically for creating an account
    path('accounts/signup/', views.signup, name='signup'),
    path('user/index/', views.user_drinks, name="user_index"),
    #Search Path
    # path('results/', views.SearchView.as_view(), name='search'),
]