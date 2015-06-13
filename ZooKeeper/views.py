# Create your views here.
#added by Jesus June 11 2015
from django.shortcuts import render_to_response
from django.http import HttpResponse


def index (request):
    return render_to_response('index.html')

def contact (request):
    return render_to_response('contact.html')

def about(request):
    return render_to_response('about.html')

def blog(request):
    return render_to_response('blog.html')