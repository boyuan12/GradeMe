from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'authentication/login.html', {'message': 'Invalid username or password'})
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'authentication/login.html', {'message': 'Logged out successfully'})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'authentication/login.html', {'message': 'User registered successfully'})
    return render(request, 'authentication/register.html')
