from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin) : 
    pass


@admin.register(models.Vote) 
class VoteAdmin(admin.ModelAdmin) : 
    pass 

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin) : 
    pass