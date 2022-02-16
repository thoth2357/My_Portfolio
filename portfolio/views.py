# importing modules
from email import message
from operator import contains
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.mail import send_mail



# import models
from .models import *
from .forms import ContactForm


# Create your views here.
@csrf_protect
def home_view(request):
    """
    function based view for home page

    Args:
        request:
    """
    config_name = "MY PORTFOLIO CONFIG"

    form = ContactForm()

    user_info = User_info.objects.get(Portfolio__Portfolio_name=config_name)
    personlization_info = Personlization.objects.get(Portfolio__Portfolio_name=config_name)
    social_info = Social_info.objects.get(Portfolio__Portfolio_name=config_name)
    services_info = Services.objects.all().filter(Portfolio__Portfolio_name="MY PORTFOLIO CONFIG")
    experience_info = Experience.objects.first()
    experience_info_work = Work.objects.all().filter(Experience__User_story=experience_info.User_story)
    experience_info_education = Education.objects.all().filter(Experience__User_story=experience_info.User_story)
    portfolio_info = 4
    profession = [i.strip() for i in user_info.profession.split(',')]
    contact_info = Contact.objects.all().get(Portfolio__Portfolio_name="MY PORTFOLIO CONFIG")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            #sending email to portfolio owner
            # send_mail('EMail From Personal Website',
            # message,
            # email,
            # [Contact.objects.all().get(Portfolio__Portfolio_name="MY PORTFOLIO CONFIG").E_mail]
            # )
            message_sent = 'True'    #django message not used cause i don't find it attractive at the moment
        else:
            message_sent = 'False'
        
        context = {'user_info': user_info, 'profession': profession,
               'social_info': social_info,
               'personlization_info': personlization_info,
               'services_info': services_info,
               'experience_info': experience_info,
               'experience_info_work': experience_info_work,
               'experience_info_education': experience_info_education,
               'portfolio_info': portfolio_info,
               'contact_info':contact_info,
               'form':form,
               'message_sent':message_sent,
        }
        return render(request, "Homepages/index.html", context)
        
            
    
    context = {'user_info': user_info, 'profession': profession,
               'social_info': social_info,
               'personlization_info': personlization_info,
               'services_info': services_info,
               'experience_info': experience_info,
               'experience_info_work': experience_info_work,
               'experience_info_education': experience_info_education,
               'portfolio_info': portfolio_info,
               'contact_info':contact_info,
               'form':form,
               }
    return render(request, "Homepages/index.html", context)
