# boilerplate
from django.urls import path
from . import views

# The URLS that are not tested and working are commented out.
# When they work, we will comment them back in and confirm stability.
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    # path('drinks/', views.drinks_index, name='index'),
    # path('drinks/<int:drink_id>/', views.drink_detail, name='details'),
    # path('drinks/create/', views.DrinkCreate.as_view(), name='drinks_create'),
    # path('drinks/<int:pk>/update', views.DrinkUpdate.as_view(), name='drinks_update'),
    # path('drinks/<int:pk>/delete', views.DrinkDelete.as_view(), name='drinks_delete'),
    
    # Still need Reviews to be added for routes later
]