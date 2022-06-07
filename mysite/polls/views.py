from django.shortcuts import render
from django.http import HttpResponse
from .models import feature

# Create your views here.from django.http import HttpResponse


def index(request):
    feature1= feature()
    feature1.id= 0
    feature1.name='fast'
    feature1.details= ' our service is very quick'

    feature2= feature()
    feature2.id= 1
    feature2.name='Reliable'
    feature2.details= ' our service is very realiabe'

    feature3= feature()
    feature3.id= 2
    feature3.name='Affordable'
    feature3.details= ' our service is very afordable'

    return render(request, 'index.html', {'feature': feature1, 'feature': feature2, 'feature': feature3})



