from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def homePageview(request):
    return HttpResponse("hey there i am Pages App")

def bingoPageView(reuqest):
    return HttpResponse("I am the another method of Pages App")
