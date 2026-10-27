from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class MyProjectView(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        return render(request , "project_module/my_projects.html" , context={
             "page_active" : "my-project"
        })


# It needs to be logged in user 
class UploadProject(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""

    def get(self , request) : 
        return render(request , "project_module/upload.html" , context={
             "page_active" : "upload-project"
        })



class ProjectDetail(generic.View) : 
    def get(self , request) : 
        return render(request , "project_module/detail_project.html" , context={
             "page_active" : "upload-project"
        })


class AllProjectView(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        return render(request , "project_module/my_projects.html" , context={
             "page_active" : "my-project"
        })




class ChatProjectView( generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        return render(request , "project_module/project_chat.html" , context={
             "page_active" : "my-project"
        })
