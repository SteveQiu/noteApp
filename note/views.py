from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

# from .models import Account
from .models import Note

def index(request):
    # return HttpResponse("Hello, world. You're at the note index.")
    if not request.user.is_authenticated():
        return render(request, 'note/index.html')
    context = {'authenticated': 'true'}
    return render(request, 'note/index.html',context)

def signup(request):
    uid = request.POST['id']
    pwd = request.POST['pwd']
    email = request.POST['email']
    try:
        user = User.objects.create_user(uid, email, pwd)
        user.save()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse("Sign up successfully. Please login in the home page")

def dashboard(request):
    if not request.user.is_authenticated():
        uid = request.POST['id']
        pwd = request.POST['pwd']
        user = authenticate(username=uid, password=pwd)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
            else:
                return HttpResponse("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            return HttpResponse("The username and password were incorrect.")
    context = {'uid': request.user.username,'note_list':request.user.note_set.all()}
    return render(request, 'note/dashboard.html',context)

def redirect(request):
    return HttpResponseRedirect("/")

def signout(request):
    logout(request)
    return HttpResponseRedirect("/")

def create(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    title = request.POST['title']
    text = request.POST['text']
    request.user.note_set.create(title = title, text = text)
    return HttpResponseRedirect("/profile/dashboard")
