from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')

    return render(request, 'users/index.html')


@login_required
def welcome(request):
    return render(request, 'users/welcome.html')
