from django.shortcuts import render, redirect
from .models import ServiceRequest
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

@login_required
def account_info(request):
    user = request.user  # Get the current authenticated user
    return render(request, 'account_info.html', {'user': user})
    

def submit_request(request):
    if request.method == 'POST':
        request_type = request.POST['request_type']
        details = request.POST['details']
        attached_file = request.FILES.get('attached_file')
        user = request.user
        ServiceRequest.objects.create(
            customer=user,
            request_type=request_type,
            details=details,
            attached_file=attached_file
        )
        return redirect('request_tracking')
    return render(request, 'submit_request.html')

def request_tracking(request):
    user = request.user
    requests = ServiceRequest.objects.filter(customer=user)
    return render(request, 'request_tracking.html', {'requests': requests})

def user_login(request):
    if request.method == 'POST':
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('submit_request')  # Redirect to the dashboard page upon successful login
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page upon successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


