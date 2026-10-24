from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import forms
from . import models
# Register your models here.
class UserAdmin(BaseUserAdmin) : 
    model = models.User
    add_form = forms.CustomCreateUserForm
    form = forms.CustomChangeUserForm
    list_display = ["username" , "first_name" , "last_name"]
    search_fields = ["username" , "first_name" , "last_name"]
    fieldsets = (
        (None, {
            "fields": ("username" , "password" )
        }),
        ("Personal information", {
            "fields": (
                "first_name",
                "last_name",
                "phone_number",
                "role",
            ),
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
        ("Important dates", {
            "fields": ("last_login",),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "first_name",
                "last_name",
                "phone_number",
                "role",
                "password1" , "password2",
                "is_staff",
                "is_superuser",
                "is_active",
            ),
        }),
    )
    
    
admin.site.register(models.User , UserAdmin)