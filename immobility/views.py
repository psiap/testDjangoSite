from django.shortcuts import render
from django.views.generic import ListView




def about(request): #HttpRequest
    return render(request, 'immobility/index.html')