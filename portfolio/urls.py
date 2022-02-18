from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path("blog/", include('blog.urls'))

]


