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
    context = {}
    return render(request, "Homepages/index.html", context)




