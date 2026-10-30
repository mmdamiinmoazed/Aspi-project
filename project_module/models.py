from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from datetime import datetime
# Create your models here.
class Project(models.Model) : 
    CATEGORY_FIELDS = [ 
        ("طراحی رابط کاربری" , 'ui/ux') , 
        
    ]
    STATUS_FIELDS = [
        ("is_verified" , "تایید شده") , 
        ("checking" , "در حال بررسی"), 
        ("rejected" , "رد شده")
    ]
    title = models.CharField(max_length=50 , )
    project_file = models.FileField(upload_to="projects/")
    
    category = models.CharField(choices=CATEGORY_FIELDS , max_length=25)
    description = models.TextField(max_length=500)
    deadline = models.DateTimeField()

    slug = models.SlugField(db_index=True,unique=True , blank=True , allow_unicode=True)

    performer = models.ForeignKey(get_user_model() , on_delete=models.CASCADE,null=True)

    status = models.CharField(choices=STATUS_FIELDS , default="checking" , max_length=25)

    created_at = models.DateTimeField(auto_now_add=True , null=True)
    def save(self,*args, **kwargs) : 
        if not self.slug : 
            self.slug = slugify(self.title , allow_unicode=True)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.title