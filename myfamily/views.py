from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
	<a href='/rango/about/'>About</a>
	return HttpResponse("Rango says hey there partner!")

def about(request) :
	<a href='/rango/'>Index</a>
	return HttpResponse("Rango says hey there partner!")
# Create your views here.
