from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#from . import views


def helloworld(request):
    return HttpResponse("Hello, World!")
