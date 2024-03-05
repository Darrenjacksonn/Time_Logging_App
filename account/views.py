from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm


def NaN_screen_view(request):
    return redirect(reverse('login'))

def register_screen_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))  # Assuming you have a URL named 'login'
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})



