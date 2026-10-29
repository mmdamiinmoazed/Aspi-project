from django import forms
from . import models

class ProjectModelForm(forms.ModelForm) : 
    CATEGORY_FIELDS = [ 
        ("طراحی رابط کاربری" , 'ui/ux') , ("گرافیک", "graphic"),
    ]
    title = forms.CharField(max_length=50 , label="عنوان" , required=True ,  
                            widget=forms.TextInput(attrs={'id' : "title" ,  "class" : "input"})
                            ,error_messages={
                                "required" : "این فیلد الزامی است"
                            })
    project_file = forms.FileField( label="فایل پروژه" , 
                                   widget=forms.FileInput(attrs={"type" : "file" , "id" : "project-file" , "accept" : ".zip,.rar,.pdf,.psd",
                                                                 "class" : "visually-hidden"}),
                                   error_messages={"required" : "این فیلد الزامی است"})
    
    category = forms.ChoiceField(choices=CATEGORY_FIELDS , label="دسته بندی " , 
                            widget=forms.Select(attrs={"class" : "input"}),
                               required=True,
                               error_messages={
                                   "required" : 'این فیلد الزامی است'
                               } , )
    description = forms.CharField(max_length=500, label="توضیحات پروژه" , 
                                  required=True ,  
                                  widget=forms.Textarea(attrs={"id" : "description" , "rows" : 5}),
                                  error_messages={
                                      "required" : "این فیلد الزامی است"
                                  })

    check_box = forms.BooleanField(required=True , error_messages={
        "required" : "این فیلد الزامی است "
    }) 
    class Meta : 
        model = models.Project
        fields = [
            "title" , "category" , "project_file" , "description"
        ]
