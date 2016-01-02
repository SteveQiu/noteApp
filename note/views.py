from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from .models import Account

def index(request):
    # return HttpResponse("Hello, world. You're at the note index.")
    context = {'init': 'hello world'}
    return render(request, 'note/index.html', context)

def signup(request):
    account = Account(uid = 'sdq',pwd = 'sdq',email = 'sdq@sdq.com')
    account.save()
    return HttpResponse("sign up")

def signin(request):
    accounts_list = Account.objects.all()
    output = ', '.join([account.uid for account in accounts_list])
    # return HttpResponse("signin")
    return HttpResponse(output)

def dashboard(request,account_id):
    return HttpResponse(" %s dashboard"% account_id)

def redirect(request):
    return HttpResponseRedirect("/")
