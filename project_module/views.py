from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class MyProjectView(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        return render(request , "account_module/my_projects.html" , context={
             "page_active" : "my-project"
        })


# It needs to be logged in user 
class UploadProject(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""

    def get(self , request) : 
        return render(request , "account_module/upload.html" , context={
             "page_active" : "upload-project"
        })
