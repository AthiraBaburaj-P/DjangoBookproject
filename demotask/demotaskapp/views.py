from django.http import HttpResponse
from django.shortcuts import render
from . models import Topic

# Create your views here.
def demo(request):
    obj = Topic.objects.all()
    return render(request,"index.html",{'result':obj})


    # return render (request,"index.html")


# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add =x+y
#     sub=x-y
#     mul=x*y
#     div= x/y
#     # consolidated= 'addition='+ add + 'subtraction='+sub+ 'multiplication=' +mul+ 'division='+div

#     return render(request,"about.html",{'addition':add, 'subtraction':sub,
#          'multiplication':mul, 'division':div})