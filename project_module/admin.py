from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin) : 
    pass