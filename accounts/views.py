from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Credenciales inválidas. Intenta de nuevo.')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def assign_admin(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.is_staff = True 
    user.is_superuser = True
    user.save()
    return redirect('user_list') 