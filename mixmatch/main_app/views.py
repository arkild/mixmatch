from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def drinks_index(request):
    # drinks index is a more complicated route
    return render(request, 'drinks/index.html', {'drinks': drinks})