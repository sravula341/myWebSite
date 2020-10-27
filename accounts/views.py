from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from . forms import createUserForm
from django.http import HttpResponse
from django.template import loader

def homepage(request):

    userid = request.headers['uid']
    roles = request.headers['role']
    #make a call to db to get user info

    template = loader.get_template('accounts/homepage.html')
    Context = {
        'uid':userid,
        'role':roles
    }
    return HttpResponse(template.render(Context,request))

def signup_view(request):
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home-page')
    else:
        form = createUserForm()
    return render(request, 'accounts/signup.html', {'form':form})

def reset_password(request):
    return render(request, 'accounts/password_reset.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home-page')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect ('login')
    #return render(request,'accounts/logout.html')




