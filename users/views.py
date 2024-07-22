from django.shortcuts import render , redirect
from django.contrib.auth import logout 
from django.contrib import messages
from django import forms
from .forms import registerForm
from django.contrib.auth import login as auth_login

# Create your views here.



def logout_view(request):
  logout(request)
  messages.warning(request, 'you are logged out now , bye')
  return redirect('main:home')

def register(request):
    if request.user.is_authenticated:
        return redirect('main:home') 
    form = registerForm()  
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration complete, thank you!')
            return redirect('main:home')

    return render(request, 'users/register.html', {'form': form})

