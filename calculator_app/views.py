from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is the Calculator app created by the Group leader Ayesha Tabassum. This line is added by Kashaf.")