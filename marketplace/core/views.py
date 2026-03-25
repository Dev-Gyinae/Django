from django.shortcuts import render, redirect
from django.contrib.auth import login
from item.models import category, item
from .forms import SignUpForm

# Create your views here.
def index(request):
    items = item.objects.filter(is_sold=False)[0:6]
    categories = category.objects.all()
    return render(request, 'core/index.html', {'categories': categories, 'items': items})

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/services.html')

def products(request):
    return render(request, 'core/products.html')    

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})