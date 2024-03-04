from . import views
from django.urls import path

urlpatterns = [
    path('', views.NaN_screen_view, name = 'NaN'),
    path('dashboard/', views.dashboard_screen_view, name = 'dashboard'),
    path('dashboard/<int:action_id>/', views.start_action, name = 'start_action'),
    path('dashboard/<int:action_time_id>/', views.stop_action, name = 'stop_action'),


    path('input/', views.input_screen_view, name = 'input'),
    path('input/<int:action_id>/', views.delete_action, name = 'input_delete_action'),


    path('reports/', views.reports_screen_view, name = 'reports'),
    
]