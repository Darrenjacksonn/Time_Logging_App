from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import ActionForm
from .models import Action, ActionTime
from django.utils import timezone


def NaN_screen_view(request):
    return redirect(reverse('login'))

@login_required
@never_cache
def dashboard_screen_view(request):

    user_actions = Action.objects.filter(user = request.user) if request.user.is_authenticated else []

    return render(request, 'product/dashboard.html', {'actions' : user_actions})


def start_action(request, action_id):

    if ActionTime.objects.filter(action__user = request.user, is_active = True).exists():
        pass
    else:
        action = Action.objects.get(id = action_id)
        ActionTime.objects.create(action = action, start_time = timezone.now(), is_active = True)
    return redirect(reverse('dashboard'))

def stop_action(request, action_time_id):
    action_time = ActionTime.objects.get(id = action_time_id, action__user = request.user, is_active = True)
    action_time.stop_time = timezone.now()
    action_time.is_active = False
    action_time.save()
    return redirect(reverse('dashboard'))








@login_required
@never_cache
def input_screen_view(request):
    # Loads all the current Tasks that the user has
    user_actions = Action.objects.filter(user = request.user) if request.user.is_authenticated else []


    form = ActionForm(request.POST or None)

    # If a button has been pressed
    if request.method == 'POST':
        if form.is_valid():
            action = form.save(commit = False)
            action.user = request.user
            action.save()
            return redirect(reverse('input'))  # Assuming you have a URL named 'login'
        

    return render(request, 'product/input.html', {'actions' : user_actions, 'form': form})

def delete_action(request, action_id):
    action = get_object_or_404(Action, id = action_id, user = request.user)
    if request.method == 'POST':
        action.delete()
        return redirect(reverse('input'))
    return redirect('input')





@login_required
@never_cache
def reports_screen_view(request):
    return render(request, 'product/reports.html')

