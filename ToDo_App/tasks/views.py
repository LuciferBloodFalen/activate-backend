from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    return render(request, 'tasks/home.html')


def dashboard_view(request):
    return render(request, 'tasks/dashboard.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    
    return render(request, 'tasks/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'tasks/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')


@login_required
def dashboard_view(request):
    user = request.user
    tasks = Task.objects.filter(user=user).order_by('-created_at')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'tasks/dashboard.html', {'tasks': tasks, 'form': form})


@login_required
def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


@login_required
def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.info(request, "Task deleted.")
    return redirect('dashboard')


@login_required
def add_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user   # Assign current logged-in user
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})