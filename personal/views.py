from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html')

def projects(request):
    return render(request, 'personal/projects.html')

def education(request):
    return render(request, 'personal/education.html')