from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def NaN_screen_view(request):
    return redirect(reverse('login'))

@login_required
def dashboard_screen_view(request):
    return render(request, 'product/dashboard.html')

@login_required
def input_screen_view(request):
    return render(request, 'product/input.html')

@login_required
def reports_screen_view(request):
    return render(request, 'product/reports.html')