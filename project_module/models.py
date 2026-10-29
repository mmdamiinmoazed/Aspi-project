from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
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

    slug = models.SlugField()

    performer = models.ForeignKey(get_user_model() , on_delete=models.CASCADE,null=True)

    status = models.CharField(choices=STATUS_FIELDS , default="checking" , max_length=25)
    def save(self,*args, **kwargs) : 
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
