from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from .models import Account

def index(request):
    # return HttpResponse("Hello, world. You're at the note index.")
    context = {'init': 'hello world'}
    return render(request, 'note/index.html', context)

def signup(request):
    print request.POST
    uid = request.POST['id']
    pwd = request.POST['pwd']
    email = request.POST['email']
    count = Account.objects.filter(uid=uid).count()
    if count>0:
        return HttpResponse("id in use")
    else:
        account = Account(uid = uid,pwd = pwd,email = email)
        account.save()
        return HttpResponse("sign up")


def signin(request):
    accounts_list = Account.objects.all()
    count = Account.objects.filter(uid='sdq').count()
    output = ', '.join([account.uid for account in accounts_list])+',Total:' + str(count)
    # return HttpResponse("signin")
    return HttpResponse(output)

def dashboard(request,account_id):
    return HttpResponse(" %s dashboard"% account_id)

def redirect(request):
    return HttpResponseRedirect("/")
