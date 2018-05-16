from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World !! Essa é a Index')

# Create your views here.
