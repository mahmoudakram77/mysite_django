from django.shortcuts import render , redirect
from .forms import loginForm
from django.contrib.auth import authenticate , login 
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')  
            user = authenticate(request, username=username, password=password)
           
            if user is not None:
                login(request, user)
                messages.success(request, 'login successful')
                return redirect('main:home')
               
            messages.warning(request , 'username or password incorrect! Try Again') 
    else:
        form = loginForm()  

    context = {
        'form': form,
    }
    return render(request, 'main/home.html', context)

      
      

    
  