from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

@login_required
def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Corrected typo here
            form.save()
            return redirect('home')  # Assuming you have a 'home' URL pattern
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # Corrected typo here
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Assuming you have a 'home' URL pattern
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def create_project(request):
    # Assuming your ProjectForm includes the team_members field
    ProjectFormSet = formset_factory(ProjectForm, extra=1)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = ProjectFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()

            # Associate team members with the project
            for team_form in formset:
                if team_form.cleaned_data.get('team_members'):
                    team_members = team_form.cleaned_data['team_members']
                    project.team_members.add(*team_members)

            return redirect('project_list')
    else:
        form = ProjectForm()
        formset = ProjectFormSet()

    return render(request, 'create_project.html', {'form': form, 'formset': formset})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'delete_project.html', {'project': project})

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})
