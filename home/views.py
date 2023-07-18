from django.shortcuts import render , redirect
from.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    blog = Blog.objects.all()

    blog = {
        "blog" : blog
    }

    return render(request,'index.html',blog)


@login_required(login_url="login")
def content(request,id):
    blog = Blog.objects.get(id=id)

    context = {
        "blog":blog
    }

    return render(request,'content.html',context)

def signup(request):

    if request.method=="POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        user = User.objects.create_user(first_name=fname,username=email,password=password)

        user.save()

        return redirect('home')
    
    return render(request,'signup.html')


def Log_in(request):

    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')

        user = authenticate(request,username=email, password=password)

        print(user)

        if user is not None:
            login(request, user)
        else:
            pass
        return redirect('home')

    return render(request,'login.html')

def Log_out(request):
    logout(request)
    return redirect("home")