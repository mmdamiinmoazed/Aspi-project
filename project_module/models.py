from django.db import models
from django.utils.text import slugify
# Create your models here.
class Project(models.Model) : 
    CATEGORY_FIELDS = [ 
        ("طراحی رابط کاربری" , 'ui/ux') , 
    ]
    title = models.CharField(max_length=50 , )
    project_file = models.FileField(upload_to="projects/")
    
    category = models.CharField(choices=CATEGORY_FIELDS , max_length=25)
    description = models.TextField(max_length=500)
    deadline = models.DateTimeField()

    slug = models.SlugField()


    def save(self,*args, **kwargs) : 
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
