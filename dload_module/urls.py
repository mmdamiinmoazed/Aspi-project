from django.urls import path
from . import views


urlpatterns = [
    path("download-file/<int:file_id>",views.DownloadView.as_view() , name="download-link")
    
]

