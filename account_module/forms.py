from django import forms
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
class LoginForm(forms.Form) : 
    username = forms.CharField(
        required=True , label="نام کاربری", max_length=50 , error_messages={"required" : "این فیلد الزامی است"} ,
        widget=forms.TextInput(attrs={"class" : "input" , "name":"username" ,  "id" : "username" , "autocomplete" : "username" , "placeholder" : "لطفا نام کاربری خود را وادر کنید"}) 
    )



    password = forms.CharField(max_length=50 , label="رمز عبور" ,  required=True , error_messages={
        "required":"این فیلد الزامی است" 
    } , widget=forms.PasswordInput(attrs={"class" : "input input--mask","id" : "password" , 
                                          "autocomplete" : "current-password" , "placeholder" : "لطفا رمز عبور خود را وارد کنید"}))
    def clean(self):

        return super().clean()   

class CustomCreateUserForm(UserCreationForm) : 
    class Meta : 
        model = User
        fields = ["first_name" , "last_name" , "role" , "is_superuser" , "is_active" ]

class CustomChangeUserForm(UserChangeForm) : 
    class Meta : 
        model = User
        fields = "__all__"