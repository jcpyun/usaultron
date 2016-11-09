from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import DashboardPost
from .forms import UploadForm


# from manifest.jsoncleaner import BloombergCleaner,startingCleaner
# from manifest.news import getNews
# from manifest.stats import *

# Create your views here.



def dashboard(request):
    
    template="dashboard_templates/base.html"
    print request.FILES,"wow"
    form = UploadForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        variable = form.save(commit='false')
        variable.save() 
    print form
    context={
        "form":form,
    }
    return render(request,template,context)

def kinetic(request):
    
    template="dashboard_templates/kinetic.html"
    print request.FILES,"wow"
    form = UploadForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        variable = form.save(commit='false')
        variable.save() 
    print form
    context={
        "form":form,
    }
    return render(request,template,context)

def potential(request):
    uploaded=DashboardPost.objects.all()
    # uploaded=DashboardPost.objects.values('file_upload')
    print uploaded
    template="dashboard_templates/potential.html"
    

    context={
        "uploaded":uploaded,
        
    
    }
    return render(request,template,context)