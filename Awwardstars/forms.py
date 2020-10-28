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