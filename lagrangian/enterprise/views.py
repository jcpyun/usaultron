from django.shortcuts import render
from .forms import BloombergForm
from .jsoncleaner import BloombergCleaner,startingCleaner
# Create your views here.
def enterprise(request):
    template="enterprise_templates/enterprise.html"
    form = BloombergForm(request.POST or None)
 
    if form.is_valid():
        variable=form
    
        company=form.cleaned_data['URL']
        print company
        # print company
        # print BloombergCleaner(company)
        query=BloombergCleaner(company)
        closing=startingCleaner(company)
 
        start=query[0]
        end=query[len(query)-1]
        # print query,"wow"
        # print query
        delta= end-closing
        percent= float(delta)/float(closing)
        percent="("+str(round(percent,5)*100)+"%)"
        querydict={
            'query':query,
            "company":company,
           
            "start":start,
            "end":end,
            "closing":closing,
            "delta":delta,
            "percent":percent,
            
        }
        # print querydict,query,"wow"
        return render(request,"enterprise_templates/bloomberg.html",querydict)
        # return redirect(reverse('/bloomberg')+ query)
    context={
        "form": form,
        
    }
    return render(request,template,context)