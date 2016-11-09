from django import forms
from django.forms import ModelForm

from .models import PolicePost, ObjectPost
class PoliceForm(ModelForm):
    class Meta:
        model = PolicePost
        fields = ['Victim','Suspect','Longitude','Latitude',"Information"
        ]
    def __init__(self, *args, **kwargs):
        super(PoliceForm, self).__init__(*args, **kwargs)
        self.fields['Victim'].widget.attrs['placeholder'] ='Victim Name'
        self.fields['Victim'].required = False
        self.fields['Victim'].label=""
        self.fields['Suspect'].widget.attrs['placeholder'] ='Suspect Name'
        self.fields['Suspect'].required = False
        self.fields['Suspect'].label=""
        self.fields['Longitude'].widget.attrs['placeholder'] ='Longitude'
        self.fields['Longitude'].required = False
        self.fields['Longitude'].label=""
        self.fields['Latitude'].widget.attrs['placeholder'] ='Latitude'
        self.fields['Latitude'].required = False
        self.fields['Latitude'].label=""
        self.fields['Information'].widget.attrs['placeholder'] ='Information'
        self.fields['Information'].required = False
        self.fields['Information'].label=""
class ObjectForm(ModelForm):
    class Meta:
        model = ObjectPost
        fields = ['Name','Age','Sex','Address','Relations','Birthday',
        ]
    def __init__(self, *args, **kwargs):
        super(ObjectForm, self).__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs['placeholder'] ='Name'
        self.fields['Name'].required = False
        self.fields['Name'].label=""
        self.fields['Birthday'].widget.attrs['placeholder'] ='YYYY-MM-DD'
        self.fields['Birthday'].required = False
        self.fields['Birthday'].label=""
        
      



class SlateForm(forms.Form):
    QUERY = forms.CharField(label='query', max_length=500)
    QUERY.label=''
    QUERY.widget.attrs['placeholder']="Insert your Command"

