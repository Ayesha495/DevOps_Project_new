from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is the Calculator app created by the Group leader Ayesha Tabassum. This line is added by Kashaf.")

def bug(request):
    #BUG ALERT: the line below should be return HttpResponse("this is not a buggy code.")
    return Http("This is a buggy view")