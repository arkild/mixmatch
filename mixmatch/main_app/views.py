from django.shortcuts import render

# Create your views here.
def home(request):
    return print('hello home')
    # return render(request, 'home.html')

def about(request):
    return print('hello about')
    # return render(request, 'about.html')

def drinks_index(request):
    return print('hello drinks')
    # drinks index is a more complicated route
    # return render(request, 'drinks/index.html', {'drinks': drinks})