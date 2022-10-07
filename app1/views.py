from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>python</h1>')

def second(request):
    return HttpResponse('<h2><marquee>django</marquee></h2>')