from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/services.html')

def products(request):
    return render(request, 'core/products.html')    

def about(request):
    return render(request, 'core/about.html')   