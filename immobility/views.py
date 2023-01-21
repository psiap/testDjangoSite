from django.shortcuts import render
from django.views.generic import ListView




def index(request): #HttpRequest
    return render(request, 'immobility/index.html')

def showcase(request): #HttpRequest
    return render(request, 'immobility/showcase.html')

#https://xn--80aq4b.xn--80adxhks/about/

def about(request): #HttpRequest
    return render(request, 'immobility/about.html')

def contact(request): #HttpRequest
    return render(request, 'immobility/contact.html')