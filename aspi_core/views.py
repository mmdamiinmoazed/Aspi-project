from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView,View
from rest_framework.request import Request
from django.http import HttpResponse
from django.contrib.auth import logout
class Home(RedirectView) : 
    url = reverse_lazy("dashboard")
class ClearSession(View) : 
    
    def get(self, request,):
        logout(request=request)
        if request.user.is_authenticated == True : 
         return HttpResponse("THIS IS PERFORMED")
        else : 
           return HttpResponse("USER not EXIST")