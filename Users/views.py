from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email already in use')
                return redirect('register')
            else:
                user_new = User.objects.create(username=username, password=password1, email=email,
                                               first_name=first_name, last_name=last_name)
                user_new.save()
                print('user created')
                return redirect('/login')
        else:
            print('Password not matched')
            return redirect('/register')

    else:
        return render(request, 'users/register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/flights')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('/login')
    else:
        return render(request, 'users/login.html')


def logout_page(request):
    auth.logout(request)
    messages.info(request, 'Successfully logged out')
    return redirect('/login')
