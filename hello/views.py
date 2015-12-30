from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):
    greeting = Greeting()

    # print Greeting()
    greeting.save()
    # print [greeting]
    # print Greeting.objects.all()
    # print Greeting.objects.all()

    # return render(request, 'index.html')
    return render(request, 'db.html', {'greetings': [greeting]})
