from django.shortcuts import render


from .forms import SlateForm
from .drones import DronesCleaner,totalDrones
from .news import *
from django.contrib.auth.decorators import login_required ## login redirect
# from manifest.jsoncleaner import BloombergCleaner,startingCleaner
# from manifest.news import getNews
# from manifest.stats import *

# Create your views here.

def demo(request):
    template="demo_templates/demo.html"
    context={}
    return render(request,template,context)
def drones(request):
    template="demo_templates/drones/dashboard.html"
    data= DronesCleaner()
    # print data
    total=totalDrones()
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        print search_query
   
    context={
        "search_query":search_query,
        "data":data,
        "total":total
   
    }
    return render(request,template,context)
def news(request):
    template="demo_templates/news/stats.html"
    clean=cleaner()
    stats=bloombergNews()
    bbc= bbcNews()
    cnn=othernews("cnn","top")
    times=othernews("the-new-york-times","popular")
    context={
        "stats":stats,
        "clean":clean,
        "bbc":bbc,
        "cnn":cnn,
        "times":times,
    }
    return render(request,template,context)

@login_required(login_url='/login/')
def intelligence(request):
    template="demo_templates/intelligence/dashboard.html"
    context={
      
    }
    return render(request,template,context)


from .models import PolicePost, ObjectPost
from .forms import PoliceForm, ObjectForm

from django.core import serializers


@login_required(login_url='/login/')
def police_dashboard(request):
    template="demo_templates/police/dashboard.html"
    context={}
    # if request.method == 'GET': # If the form is submitted
    suspect = request.GET.get('suspect_search_box', None)
    victim =request.GET.get('victim_search_box', None)
        
    suslong=0
    suslat=0
    histogram=PolicePost.objects.all()
    data = serializers.serialize("python", PolicePost.objects.all(),fields=('Information')) ## important!!!!
    ####3
    raw_data = serializers.serialize('python', PolicePost.objects.all())
    actual_data = [d['fields'] for d in raw_data]
    output = json.dumps(actual_data)####
    # data = serializers.serialize('python', SomeModel.objects.all(), fields=('name','size'))
    # queryResult={}
    # for x in xrange(len(histogram)):
    #     for y in PolicePost._meta.fields:
    #         attr=y.name
    #         print attr,"wow",type(attr)
    #         queryResult.setdefault(y.name,histogram[x].Victim)
    # print queryResult

    try:
        alllat=[]
        alllong=[]
        for x in histogram:
            if x.Suspect.lower()==suspect.lower():
                suslong=x.Longitude
                alllong.append(float(suslong))
                suslat=x.Latitude
                alllat.append(float(suslat))
                
    except:
        pass
    
    """
    suspectinfo=[]
    victiminfo={}
    for x in histogram:
        if x.Suspect==suspect:
            suspectinfo.append(x)
    """
            
            
    
    context={
        "data":data,
        "raw_data":raw_data,
        "actual_data":actual_data,
        "output":output,
        "suspect":suspect,
        "victim":victim,
        "histogram":histogram,
        "suslong":suslong,
        "suslat":suslat,
        "alllat":alllat,
        "alllong":alllong,
       
    }
    return render(request,template,context)
@login_required(login_url='/login/')
def police_home(request):
    form = PoliceForm(request.POST or None)
    objectform= ObjectForm(request.POST or None)
   
        

    print form
    if form.is_valid() and 'button1' in request.POST:
        variable=form.save(commit='false')
        variable.save()
    if objectform.is_valid() and 'button2' in request.POST:
        objectvariable=objectform.save(commit="false")
        objectvariable.save()
    template="demo_templates/police/home.html"
    histogram=PolicePost.objects.all()
    print histogram[1].pk
    context={
        "form":form,
        "histogram":histogram,
        "objectform":objectform,

    }
    return render(request,template,context)

@login_required(login_url='/login/')
def police_graph(request):
    template="demo_templates/police/graph.html"
    histogram=PolicePost.objects.all()
    print histogram[1].pk
    context={
   
        "histogram":histogram,
   

    }
    return render(request,template,context)

@login_required(login_url='/login/')
def police_fermi(request):
    template="demo_templates/police/fermi.html"
    histogram=PolicePost.objects.all()
    print histogram[1].pk
    context={
   
        "histogram":histogram,
   

    }
    return render(request,template,context)
