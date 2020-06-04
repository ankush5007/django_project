from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def homePageview(request):
    dict = {"name":"ankush","age":34,"sex":"male"}
    return render(request,'home.html',dict)

def addPageview(request):
    output = {"data": ""}
    """
    value1 = request.GET['val1'] if request.GET['val1'] != '' else 0
    value2 = request.GET['val2'] if request.GET['val2'] != '' else 0
    output["data"] = int(value1) + int(value2)
    return render(request,'result.html',output)
    """
    if request.method == "POST":
        val1 =  request.POST["val1"] if request.POST['val1'] != '' else 0
        val2 = request.POST['val2'] if request.POST['val2'] != '' else 0
        output["data"] = int(val1) + int(val2)
        return render(request,'result.html',output)


def bingoPageView(reuqest):
    return HttpResponse("I am the another method of Pages App")

def dataPageView(request):
    return HttpResponse("I am another method my name is data!!")
