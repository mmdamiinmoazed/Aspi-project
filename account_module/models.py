from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from . import manager
from django.contrib.auth.hashers import identify_hasher , mask_hash
# Create your models here.
class User(AbstractBaseUser , PermissionsMixin ) : 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    username = models.CharField(max_length=50 , unique=True)
    
    role = models.CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = manager.UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    def __str__(self):
        role = None
        if self.is_superuser : 
            role = "Admin"
        return f"{self.first_name} {self.last_name} | Role : {role} | Activity : {self.is_active}"


    def save(self , *args, **kwargs) : 

        return super().save(*args, **kwargs)

