from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
'''
def home(request):
    return HttpResponse('Hello, World!')
    return render(request, 'hello.html', {'name': 'Pietro'})
'''

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"