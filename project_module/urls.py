from django.urls import path
from . import views
urlpatterns = [
    path("upload/" , views.UploadProject.as_view() , name="upload-project"),
    path("my-projects/" , views.MyProjectView.as_view() , name="my-projects")
]
