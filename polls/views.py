from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ham1(request):
    return HttpResponse("<h1>Ham linh tinh</h1><p>xin chao cac ban</p>")