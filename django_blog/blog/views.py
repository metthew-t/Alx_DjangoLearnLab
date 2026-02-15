# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'blog/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # Update user information
        user = request.user
        user.email = request.POST.get('email', user.email)
        # Optionally update username (be careful: might need to check uniqueness)
        # user.username = request.POST.get('username', user.username)
        user.save()
        messages.success(request, 'Your profile has been updated!')
        return redirect('profile')
    return render(request, 'blog/profile.html', {'user': request.user})