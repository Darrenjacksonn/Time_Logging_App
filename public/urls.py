from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_screen_view, name = 'home'),
    path('about_us', views.about_us_screen_view, name = 'about_us'),
    path('contact_us', views.contact_us_screen_view, name = 'contact_us'),
]


