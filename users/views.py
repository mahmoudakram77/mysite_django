from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import logout 
from django.contrib import messages
from django import forms
from .forms import registerForm , recordForm
from django.contrib.auth import login as auth_login
from .models import Record
from django.urls import reverse


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


def record(request):
    records = Record.objects.all()
    return render(request, 'users/record.html', {'records':records})


def record_detail(request,pk):
    record = get_object_or_404(Record, pk=pk)

    return render(request, 'users/record_detail.html', {'record':record})


def create_record(request):
    form = recordForm()
    if request.method == 'POST':
      form = recordForm(request.POST)
      if form.is_valid():
          form.save()
          messages.info(request, 'new record add successful')
          return redirect('users:record')
      else:
          form = recordForm()
    context = {
        'form':form,
    }

    return render(request, 'users/create_record.html' , {'form':form})




def editRecord(request, pk):
    record = get_object_or_404(Record, pk=pk)  
    if request.method == 'POST':
        form = recordForm(request.POST, instance=record)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Edit Successful')
            return redirect('users:record')
    else:
        form = recordForm(instance=record)  

    context = {
        'record': record,
        'form': form,
    }
    
    return render(request, 'users/edit_record.html', context)
    
      
          


def deleteRecord(request, pk):
    record = get_object_or_404(Record ,pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, 'record is deleted')
        return redirect(reverse('users:record'))


    return render(request, 'users/confirm_delete.html', {'record':record} )