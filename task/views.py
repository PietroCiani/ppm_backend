from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from django.utils.timezone import now

# Create your views here.

def home(request):  # note: works fine with filter(assigned_to=request.user)
    if request.user.is_authenticated:
        sort_param = request.GET.get('sort')
        if sort_param == 'completed':
            todos = Todo.objects.filter(assigned_to=request.user.id).order_by('completed')
        elif sort_param == 'due_date':
            todos = Todo.objects.filter(assigned_to=request.user.id).order_by('due_date')
        else:
            todos = Todo.objects.filter(assigned_to=request.user.id)  # Retrieve only todos assigned to the logged user
    else:
        todos = None
    context = {'todos': todos}
    return render(request, 'home.html', context)


def signup(request):
    return render(request, 'signup.html')


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, initial={'created_by': request.user.id}) # Create a form instance and populate it with data from the request
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(initial={'created_by': request.user.id})

    context = {'form': form}
    return render(request, 'add.html', context)


def edit_todo(request, pk):
    todo = Todo.objects.get(id=pk) # Retrieve the todo with the given id
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)

    context = {'form': form}
    return render(request, 'edit_todo.html', context)


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)  # Retrieve the Todo object or return a 404 error if not found
    
    if request.user == todo.created_by or request.user == todo.assigned_to:
        todo.delete()
    
    return redirect('home')


def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST) # Create a form instance and populate it with data from the request
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TagForm()
        
    context = {'form': form}
    return render(request, 'add.html', context)


def edit_tag(request, pk):
    tag = Tag.objects.get(id=pk) # Retrieve the Tag with the given id
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TagForm(instance=tag)

    context = {'form': form}
    return render(request, 'edit.html', context)


class SignUpView(generic.CreateView):
    form_class = UserCustomCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
