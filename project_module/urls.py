from django.urls import path
from . import views
urlpatterns = [
    path("upload/" , views.UploadProject.as_view() , name="upload-project"),
    path("my-projects/" , views.MyProjectView.as_view() , name="my-projects"),
    path("detail/" , views.ProjectDetail.as_view() , name="my-project"),
    path("chat/" , views.ChatProjectView.as_view() , name="chat-project")
]
