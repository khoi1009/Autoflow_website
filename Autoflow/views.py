from django.shortcuts import render
from . import machine_learning_models


def Home(request):
    return render(request,'index.html')

def Contact(request):
    return render(request,'contact.html')

def result(request):
    user_input=request.GET["user_input"]
    user_input=machine_learning_models.multiplier(user_input)

    return render(request,'results.html',{'home_input':user_input})
