from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! from Django on Render 🚀")
# Create your views here.
