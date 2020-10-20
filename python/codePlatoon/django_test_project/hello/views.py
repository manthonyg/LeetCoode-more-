from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Hello world!')
def yang(request):
    return HttpResponse('Hello yang!')

def name(request,name):
    return HttpResponse(f'Hello {name}!')