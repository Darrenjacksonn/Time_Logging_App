from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    return render(request,'public/home.html')



def about_us_screen_view(request):
    return render(request,'public/about_us.html')



def contact_us_screen_view(request):
    return render(request,'public/contact_us.html')
