from django.shortcuts import render
from .models import Slider

# Create your views here.

def home(request):
    slider = Slider.objects.all()
    data = {
        'slider': slider
    }
    return render(request,'webpages/home.html', data)

def about(request):
    return render(request,'webpages/about.html')

def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    return render(request,'webpages/contact.html')