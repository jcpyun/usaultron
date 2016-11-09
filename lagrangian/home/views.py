from django.shortcuts import render
from .pdata import generateSymbolDaily

# Create your views here.
def home(request):
    template="home_templates/lagrangian.html"
    wow=generateSymbolDaily()
    lenwow=len(wow)
    context={
        "wow":wow,
        "lenwow":lenwow

    }
    return render(request,template,context)
def lamb(request):
    template="home_templates/lambda.html"
    context={}
    return render(request,template,context)