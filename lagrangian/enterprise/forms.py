from django import forms

class BloombergForm(forms.Form):
    URL = forms.CharField(label='Your name', max_length=500)
    URL.label=''
    URL.widget.attrs['placeholder']="Insert your Command"


