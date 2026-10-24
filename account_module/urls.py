from django.urls import path
from . import views


urlpatterns = [
    path("login/" , views.LoginView.as_view() , name="login-page")   ,
    path("dashboard/" , views.PanelView.as_view() , name="dashboard"),
    path("logout/" , views.LogOutFunction.as_view() , name="logout-func"),
    path("upload/projects" , views.UploadProject.as_view() , name="upload-project"),
    path("my-projects/" , views.MyProjectView.as_view() , name="my-projects")
]
