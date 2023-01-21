from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index ,name='home'),
    path('showcase/', showcase ,name='showcase'),
    path('about/', about ,name='about'),
    path('contact/', about ,name='contact'),
]