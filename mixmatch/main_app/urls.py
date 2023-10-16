# boilerplate
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    # path('drinks/', views.drinks_index, name='index'),
    # The rest are class based views - I'll do them later
]