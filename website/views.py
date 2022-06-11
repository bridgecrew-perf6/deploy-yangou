from django.shortcuts import render, redirect
from django.http import HttpResponse
from website.models import *




def hello_world(request):
  return HttpResponse('Hello, World!')

def home(request):
  characters = Character.objects.all()
  return render(request,'website/home.html',{ 'characters': characters })