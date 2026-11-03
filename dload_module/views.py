from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import FileResponse
from django.views import generic
from django.http import Http404
from project_module import models
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class DownloadView(LoginRequiredMixin,generic.View) : 
    """This comment is made by my new keyboard"""

    def get(self, request, file_id):
        project = models.Project.objects.filter(pk=file_id).first()

        if not project or not project.project_file:
            raise Http404("فایل پیدا نشد.")

        file_field = project.project_file

        try:
            file_handle = file_field.open("rb")
        except (FileNotFoundError, OSError):
            raise Http404("فایل روی سرور پیدا نشد.")

        # نام و پسوند فایل اصلی
        filename = file_field.name.rsplit("/", 1)[-1]

        return FileResponse(
            file_handle,
            as_attachment=True,
            filename=filename,
            content_type="application/octet-stream",
        )