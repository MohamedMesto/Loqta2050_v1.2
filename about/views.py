from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 

def tell_about_me(request):
    # return HttpResponse("about Loqta2050.com Team")

    return render(request,'tell_about_me.html',{'Name': 'MMM2050'})