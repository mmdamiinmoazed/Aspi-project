from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.request import Request
from django.http import HttpResponse
from . import forms,models
from django.contrib.auth import get_user_model , login , authenticate  , logout , decorators
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
User = get_user_model()
class LoginView(generic.View) : 
    def get(self , request:Request) : 
        form = forms.LoginForm()
        return render(request , "account_module/login.html" , context={
                "form" : form
        })

    
    def post(self , request:Request) : 
        form = forms.LoginForm(request.POST)
        if form.is_valid(): 
            username= form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username)
            print(password)
            user = authenticate(username=username , password=password)
            print(type(user))
            if user is not None :
                login(request, user) 
                return redirect("dashboard")
            else : 
               return render(request , "account_module/login.html" , context={
                   "form" : form , "error" : "نام کاربری یا رمز عبور اشتباه است!"
               })
        return render(request , "account_module/login.html" , context={
            "form" : form 
        })

# It needs to be logged in user 

# It needs to be logged in user 
class PanelView(LoginRequiredMixin,generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , requets:Request) : 
        user = self.request.user
        if not user.is_authenticated : 
            return redirect("login-page")
        
        print(user.username)
        return render(self.request , "account_module/dashboard.html" , context={
            "user" : user , "page_active" : "dashboard"
        })


class LogOutFunction(generic.View) : 
    def get(self , request:Request) : 
        logout(request)
        return redirect("dashboard")

