from django.db import models

# Create your models here.
class Project(models.Model) : 
    CATEGORY_FIELDS = [ 
        ("طراحی رابط کاربری" , 'ui/ux') , 
    ]
    title = models.CharField(max_length=50 , )
    category = models.CharField(choices=CATEGORY_FIELDS , max_length=25)
    description = models.TextField(max_length=500)
    