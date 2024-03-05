from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.NaN_screen_view),
    path('register/', views.register_screen_view, name = 'register'),
    path('login/', LoginView.as_view(template_name = 'account/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),

]
