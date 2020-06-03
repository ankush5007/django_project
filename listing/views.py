from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def listingview(request):
    return HttpResponse("i am from listing app")

def chainview(request):
    return HttpResponse("i am on Chaining Process!")
