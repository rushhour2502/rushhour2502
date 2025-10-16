from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello bro 👋🏽, welcome to my first Django app! h")

# Create your views here.
