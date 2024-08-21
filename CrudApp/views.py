from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def RegisterNewUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_user')
    else:
        form = UserForm()
    return render(request, 'addUser.html', {'form': form})

def ViewUser(request):
    users = User.objects.all()
    return render(request, 'display_user.html', {'users': users})

def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('display_user')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

def delete_user(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('display_user')
    return render(request, 'delete_user.html', {'user': user})
