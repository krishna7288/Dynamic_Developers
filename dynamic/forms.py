from django import forms
from .models import contact,job,details


class ContctForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ["name","mail","message"]
        
class JobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = ["firstname","secondname", "phone", "experience", "mail","Resume"]        
        
class DetailsForm(forms.ModelForm):
    class Meta:
        model = details
        fields = ["name","mail","tellAboutUs","message"]        