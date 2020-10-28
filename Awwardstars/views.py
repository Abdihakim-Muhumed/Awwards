from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Projects,Profile
from django.contrib.auth.models import User
from .forms import EditProfileForm
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = EditProfileForm()
    return render(request, 'edit_profile.html', {"form": form})
