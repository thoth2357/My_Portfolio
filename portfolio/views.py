#importing modules
from django.shortcuts import render

#import models
from .models import *
# Create your views here.

def home_view(request):
    """
    function based view for home page

    Args:
        request:
    """
    config_name = "MY PORTFOLIO CONFIG"  

    user_info = User_info.objects.get(Portfolio__Portfolio_name=config_name)
    personlization_info = Personlization.objects.get(Portfolio__Portfolio_name=config_name)
    social_info = Social_info.objects.get(Portfolio__Portfolio_name=config_name)
    services_info = Services.objects.all().filter(Portfolio__Portfolio_name="MY PORTFOLIO CONFIG")
    experience_info = Experience.objects.first()
    experience_info_work = Work.objects.all().filter(Experience__User_story=experience_info.User_story)

    
    profession = [i.strip() for i in user_info.profession.split(',')]
    
    context = {'user_info':user_info, 'profession':profession, 
    'social_info':social_info, 
    'personlization_info':personlization_info,
    'services_info':services_info,
    'experience_info':experience_info,
    'experience_info_work':experience_info_work

    }
    return render(request, "Homepages/index.html", context)



