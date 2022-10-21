from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    response = requests.get('https://inshorts.deta.dev/news?category=science')
    posts = response.json()
    data = posts['data']
    return render(request,'index.html', {'posts': data})

def contact(request):
    return render(request,'contact.html')

def category(request):
    return render(request,'category.html')

def single(request):
    return render(request,'single.html')

