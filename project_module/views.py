from django.shortcuts import render, redirect , get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from json import loads , JSONDecodeError
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
import jdatetime
from django.http import HttpResponse
# Create your views here.


# TEST FUNCTION
def project_votes(project) : 
    votes = models.Vote.objects.filter(project=project)
    likes = 0
    dislikes = 0
    for vote in votes : 
        if vote.vote_type == "like" : 
            likes = likes + 1
        else : 
            dislikes = dislikes + 1
    information = {
        "votes_count" : votes.count(),
        "likes" : likes , 
        "dislikes" : dislikes
        

    }
    return information
class MyProjectView(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        user = self.request.user
        projects = models.Project.objects.filter(performer = user.id)   
        print(projects)
        
        return render(request , "project_module/my_projects.html" , context={
             "page_active" : "my-project" , "projects" : projects
        })


# It needs to be logged in user 
class UploadProject(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""

    def get(self , request) : 
        form = forms.ProjectModelForm()
        
        return render(request , "project_module/upload.html" , context={
             "page_active" : "upload-project" ,"form" : form
        })
    def post(self , request) : 
        form = forms.ProjectModelForm(request.POST , request.FILES)
 

        if form.is_valid() :
            deadline = request.POST.get("deadline")
            # deadline = convert_time(the_deadline=deadline)
            project = form.save(commit=False)


            deadline = jdatetime.datetime.strptime(
                deadline , "%Y/%m/%d"
            ).date()
            deadline = deadline.togregorian()

            project.deadline = deadline
            project.performer = request.user
            project.save() 
            form.save()
            return redirect("dashboard")
        return render(request , "project_module/upload.html" , context={
             "page_active" : "upload-project" ,"form" : form
        })

class ProjectDetail(LoginRequiredMixin,generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request,slug=None) : 
        project = models.Project.objects.filter(slug=slug).first()
        
        project_information = project_votes(project=project)
        
        user = self.request.user

        voted = models.Vote.objects.filter(project=project , user=user).first()
        user_vote = None
        if voted : 
            user_vote = voted.vote_type

        comments = models.Comment.objects.filter(project=project)

        return render(request , "project_module/detail_project.html" , context={
             "page_active" : "upload-project" , "project" : project,"project_info" : project_information,
             "user_vote" : user_vote , "comments" : comments
             
        })

class AllProjectView(LoginRequiredMixin , generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        projects = models.Project.objects.all().order_by("-id")
        
        return render(request , "project_module/all_projects.html" , context={
             "page_active" : "all-project" , "projects" : projects
        })

class SubmitComment(LoginRequiredMixin,generic.View) : 
    login_url = reverse_lazy("login-page")

    def post(self , request , project_id=None) : 

            project = get_object_or_404(models.Project, id=project_id)
            

            comment_text = None
            if request.body:
                try:
                    data = loads(request.body.decode('utf-8'))
                    comment_text = data.get('message') or data.get('comment') or data.get('body')
                except JSONDecodeError:
                    return JsonResponse(data={
                        "status" : "error" , "message": "Decode error in programme "  , 
                    })

            if not comment_text:
                comment_text = request.POST.get('message') or request.POST.get('comment') or request.POST.get('body')

            if not comment_text or not str(comment_text).strip():
                return JsonResponse({'status': 'error', 'message': 'این فیلد نباید خالی باشه'}, status=400)

            comment = models.Comment.objects.create(
                user=request.user,
                project=project,
                message=str(comment_text).strip()
            )

            return JsonResponse({
                'status': 'success',
                'message': 'نظر شما با موفقیت ثبت شد',
                'comment': comment.message,
                'author': request.user.username
            })
class ChatProjectView(LoginRequiredMixin,  generic.View) : 
    login_url = reverse_lazy("login-page")
    redirect_field_name = ""
    def get(self , request) : 
        return render(request , "project_module/project_chat.html" , context={
             "page_active" : "my-project"
        })

# Fetch api -> handling front end with js ("check fetch_vote.js" if there was any bug in this code)
class SubmitVote(LoginRequiredMixin,generic.View) : 
    login_url = reverse_lazy("login-page")
    def post(self , request , project_id , *args, **kwargs) : 
        try : 
            vote_type = request.POST.get("vote_type")
            data = loads(request.body)
            # "action" : "dislike"   or "action" : "like"
            action = data.get("action")
            if action not in ["like" , "dislike"] : 
                return JsonResponse({"status" : "error" , "message" : "this action is not valid"})
            project = models.Project.objects.filter(id=project_id).first()
            
            vote,created = models.Vote.objects.get_or_create(
                    user=request.user,project=project
                )
            if action in ['like' , "dislike"] : 

                # It means this vote has existed before and there is not needing to create a new one
                # maybe user wants to change its comment about that project
                if not (created==True) : 
                    """This means user wants to take their vote back and it gives no vote to that user"""
                    if vote.vote_type == action : 
                        vote.delete()
                        current_vote = None

                    else :
                        vote.vote_type = action
                        vote.save()
                        current_vote = action
                    project_info = project_votes(project=project)
                    return JsonResponse(
                        
                        {
                            "status" : "success" , 
                            "message" : "user changes its vote",
                            "likes" : project_info["likes"],
                            "dislikes" : project_info["dislikes"],
                            "user_vote" : current_vote
                        } , status=200
                    )
                else : 
                    return JsonResponse(
                        
                        {
                            "status" : "success" , 
                            "message" : "user made a vote",
                            "likes" : project_info["likes"],
                            "dislikes" : project_info["dislikes"],
                            "user_vote" : current_vote
                        } , status=200
                    )
            else :
            

                return JsonResponse(
                    {
                        "status" : "error" , 
                        "message" : "There is a problem with function in backend"
                    },status=400
                )
        except Exception as e : 
            return JsonResponse(
                {
                    "status" : "error" , "message" : f"{e}"
                } , status=400
            )