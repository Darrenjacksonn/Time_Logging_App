from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import ActionForm
from .models import Action
#from django.http import HttpResponseRedirect


def NaN_screen_view(request):
    return redirect(reverse('login'))

@login_required
@never_cache
def dashboard_screen_view(request):
    return render(request, 'product/dashboard.html')





@login_required
@never_cache
def input_screen_view(request):
    # Loads all the current Tasks that the user has
    user_actions = Action.objects.filter(user = request.user) if request.user.is_authenticated else []


    form = ActionForm(request.POST or None)

    # If a button has been pressed
    if request.method == 'POST' and 'add_action' in request.POST:
        if form.is_valid():
            action = form.save(commit = False)
            action.user = request.user
            action.save()
            return redirect(reverse('input'))  # Assuming you have a URL named 'login'
        

    return render(request, 'product/input.html', {'actions' : user_actions, 'form': form})


def delete_action_view(request, action_id):
    action = get_object_or_404(Action, id = action_id, user = request.user)
    if request.method == 'POST' and 'delete_action' in request.POST:
        action.delete()
        return redirect(reverse('input'))
    else:
        return redirect('input')





@login_required
@never_cache
def reports_screen_view(request):
    return render(request, 'product/reports.html')

