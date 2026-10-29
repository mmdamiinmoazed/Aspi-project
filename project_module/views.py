from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
import jdatetime
from django.http import HttpResponse
# Create your views here.
class MyProjectView(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        user = self.request.user
        projects = models.Project.objects.filter(performer = user.id)   
        print(projects)
        
        return render(request , "project_module/my_projects.html" , context={
             "page_active" : "my-project" , "projects" : projects
        })


# It needs to be logged in user 
class UploadProject(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""

    def get(self , request) : 
        form = forms.ProjectModelForm()
        
        return render(request , "project_module/upload.html" , context={
             "page_active" : "upload-project" ,"form" : form
        })
    def post(self , request) : 
        form = forms.ProjectModelForm(request.POST , request.FILES)
 

        if form.is_valid() :
            deadline = request.POST.get("deadline")
            # deadline = convert_time(the_deadline=deadline)
            project = form.save(commit=False)


            deadline = jdatetime.datetime.strptime(
                deadline , "%Y/%m/%d"
            ).date()
            deadline = deadline.togregorian()

            project.deadline = deadline
            project.performer = request.user
            project.save() 
            form.save()
            return redirect("dashboard")
        return render(request , "project_module/upload.html" , context={
             "page_active" : "upload-project" ,"form" : form
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
        projects = models.Project.objects.all().order_by("-id")
        
        return render(request , "project_module/all_projects.html" , context={
             "page_active" : "all-project" , "projects" : projects
        })




class ChatProjectView( generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        return render(request , "project_module/project_chat.html" , context={
             "page_active" : "my-project"
        })
