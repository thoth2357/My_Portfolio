#importing modules
from django.shortcuts import render

#external Modules
import pyrebase

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

    
    fullname = user_info.Fullname
    Cv = user_info.Curriculum_vitae
    
    context = {'color':color, 'fullname':fullname, 'Cv':Cv}
    return render(request, "Homepages/index.html", context)



