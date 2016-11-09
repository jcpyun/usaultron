from django import forms
from django.forms import ModelForm


from .models import DashboardPost
class UploadForm(ModelForm):
    class Meta:
        model = DashboardPost
        fields = ['title','file']
    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] ='Title'
        self.fields['title'].label=""
        
        self.fields['file'].label=""

#         self.fields['company'].widget.attrs['placeholder'] ='Please insert the company name here'
#         self.fields['company'].label='' #this erases the item tag
#         self.fields['recruiter'].widget.attrs['placeholder'] ='Your name here'
#         self.fields['recruiter'].label='' #this erases the item tag
