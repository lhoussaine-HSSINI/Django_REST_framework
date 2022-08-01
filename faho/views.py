from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "faho/index.html",
                  {'name':'hssini dyali'})
def about(request):
    return HttpResponse('about hssini')