from django.urls import path
from .views import *


app_name = 'emailapp'

urlpatterns = [
    path('', index, name='index'),
    path('contactus/', index, name='contact_us'),
    path('<path:unknown_path>/', redirect_error, name='redirect_error'),
]
