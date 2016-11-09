from django.shortcuts import render

# Create your views here.
def base(request):
    template="fermi_templates/base.html"
    context={
    }
    return render(request,template,context)
def archive(request):
    template="fermi_templates/archive.html"
    context={
    }
    return render(request,template,context)