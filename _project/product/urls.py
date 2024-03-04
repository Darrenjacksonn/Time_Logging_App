from . import views
from django.urls import path

urlpatterns = [
    path('', views.NaN_screen_view, name = 'NaN'),
    path('dashboard/', views.dashboard_screen_view, name = 'dashboard'),
    path('input/', views.input_screen_view, name = 'input'),
    path('input/<int:action_id>/', views.delete_action_view, name = 'input_delete_action'),
    path('reports/', views.reports_screen_view, name = 'reports'),
    
]