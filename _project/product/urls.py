from . import views
from django.urls import path

urlpatterns = [
    path('', views.NaN_screen_view, name = 'NaN'),
    path('dashboard/', views.dashboard_screen_view, name = 'dashboard'),
    path('input/', views.input_screen_view, name = 'input'),
    path('reports/', views.reports_screen_view, name = 'reports'),
    
]