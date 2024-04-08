from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, CreateProject
from .models import ProjectCreate

@login_required
def index(request):
    user_projects = ProjectCreate.objects.filter(owner=request.user)
    return render(request, 'index.html', {'user_projects': user_projects})

def signup_main(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_main(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to home page after successful login
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_main(request):
    logout(request)
    # Redirect to login page after logout
    return redirect('login')

@login_required
def create_project(request):
    if request.method == 'POST':
        form = CreateProject(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            if form.cleaned_data['owner'] is None:
                project.owner = request.user
            project.save()
            return redirect('home')
    else:
        form = CreateProject()
    return render(request, 'createproject.html', {'form': form})
