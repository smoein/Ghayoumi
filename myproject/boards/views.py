from django.http import HttpResponse
from django.shortcuts import render
from .models import Board

def home(request):
    return render(request, 'home.html')