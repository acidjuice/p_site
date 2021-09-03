from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Artwork

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def about(request):
    return render(request, 'portfolio/about.html')

def artwork(request):
    artworks = Artwork.objects.all()
    return render(request, 'portfolio/artworks.html', {'artworks':artworks})
