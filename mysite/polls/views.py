from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.from django.http import HttpResponse


def index(request):
    name='borquez'
    return render(request, 'index.html',{'name':name})
