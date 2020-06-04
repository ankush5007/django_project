from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def calcPageView(request):
    return HttpResponse("I am here for calculations!")
