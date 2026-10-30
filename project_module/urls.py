from django.urls import path
from . import views
urlpatterns = [
    path("upload/" , views.UploadProject.as_view() , name="upload-project"),
    path("my-projects/" , views.MyProjectView.as_view() , name="my-projects"),
    path("detail/<str:slug>/" , views.ProjectDetail.as_view() , name="project-detail"),
    path("chat/" , views.ChatProjectView.as_view() , name="chat-project"),
    path("all-projects/" , views.AllProjectView.as_view() , name="all-projects" )
]
