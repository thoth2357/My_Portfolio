#importing modules
from django.shortcuts import render



#external Modules
import pyrebase
# Create your views here.

def home_view(request):
    """
    function based view for home page

    Args:
        request:
    """
    color = 'yellow'
    context = {'color':color}
    return render(request, "Homepages/index.html", context)



