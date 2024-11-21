from django.urls import path
from . import views

# URLConf
urlpatterns = [

path('about_me/', views.tell_about_me)

]