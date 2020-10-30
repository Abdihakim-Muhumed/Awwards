from django import forms
from .models import Profile,Projects
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user']
DESIGN_RATES=[
    (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10')
]

class RateForm(forms.Form):
    design= forms.CharField(label='Design:', widget=forms.RadioSelect(choices=DESIGN_RATES,attrs={'class': 'form-inline'}))
    usability= forms.CharField(label='Usability:', widget=forms.RadioSelect(choices=DESIGN_RATES,attrs={'class': 'form-inline'}))
    content= forms.CharField(label='Content:', widget=forms.RadioSelect(choices=DESIGN_RATES,attrs={'class': 'form-inline','style':'display: inline;'}))

