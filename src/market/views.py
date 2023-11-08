from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse


# Create your views here.

# class HomePageView(ListView):
#
#     template_name = 'market/templates/index.html'

def index(request):
    return render(request, 'market/index.html')
