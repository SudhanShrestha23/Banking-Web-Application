from django.shortcuts import render

# Create your views here.
from . import views
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You are in the database page")