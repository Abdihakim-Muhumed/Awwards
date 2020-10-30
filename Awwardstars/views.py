from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Projects,Profile
from django.contrib.auth.models import User
from .forms import EditProfileForm,NewProjectForm,RateForm
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
# Create your views here.
def index(request):
    projects = Projects.objects.all()
    return render(request,'index.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def view_project(request,project_id):
    project = Projects.objects.filter(id=project_id).first()
    form = RateForm()
    return render(request,'project.html',{"project":project,"form":form})

@login_required(login_url='/accounts/login/')
def rate_project(request,project_id):
    d = int(request.POST.get('design'))
    u = int(request.POST.get('usability'))
    c = int(request.POST.get('content'))
    total = d + u + c
    average = total / 3
    project = Projects.objects.filter(id=project_id).first()
    project.total_score += average
    project.reviews += 1
    project.save()
    project.average = project.total_score / project.reviews
    project.save()
    data = {'success':'Review submitted'}
    return redirect('view-project', project_id)

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.filter(user = current_user).first()
    except:
        return redirect('edit-profile')
    projects = Projects.objects.filter(user = current_user).all()
    total_projects = projects.count()
    return render(request,'profile.html',{"profile":profile,"projects":projects,"current_user":current_user,"total_projects":total_projects,})


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

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('profile')

    else:
        form = NewProjectForm()
        title = 'Post Project'
    return render(request, 'new_project.html', {"form": form,"title":title})


def search_results(request):

    if 'searchproject' in request.GET and request.GET["searchproject"]:
        search_term = request.GET.get("searchproject")
        searched_projects = Projects.objects.filter(title__icontains=search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
