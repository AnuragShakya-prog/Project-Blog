from django.shortcuts import render
from .models import BlogPost,Comment
from django.http import HttpResponse
from user.models import UserProfile
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib import messages
import json
# Create your views here.



def add_user_profile(request,context):
    if request.user.is_authenticated:
        try:
            user_profile=UserProfile.objects.get(user=request.user)
            context['user_profile']=user_profile
        except:
            pass
        finally:
            return context
    return context

def home(request):
    all_posts=BlogPost.objects.all()
    context={
        "posts":all_posts,
    }
    context=add_user_profile(request,context)
    return render(request,"blog/index.html",context)


def postView(request,id):
    post=BlogPost.objects.get(id=id)
    if request.method=='POST':
        comment_text=request.POST.get('commentbox','')
        if comment_text.strip()=='':
            comments=Comment.objects.filter(main_post=post)
        
            context={"post":post,'comments':comments}
            context=add_user_profile(request,context)
        
            return render(request,"blog/postView.html",context)
        comment=Comment(main_post=post,author=request.user,comment_text=comment_text)
        comment.save()
    comments=Comment.objects.filter(main_post=post)
    context={"post":post,'comments':comments}
    context=add_user_profile(request,context)
    return render(request,"blog/postView.html",context)


def profile_view(request):
    user=request.user
    context={"user":user}
    context=add_user_profile(request,context)
    return render(request,'blog/profile.html',context)


def create_post(request):
    if request.method=='GET':
        form=PostForm()
        context={'form':form}
        return render(request,'blog/createpost.html',context)
    elif request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.author=request.user
            new_post.save()
            messages.add_message(request,messages.INFO,"Post created successfully")
            return redirect("/")

        else:
            errors_data=dict(form.errors.as_data())
            id_errorDict={}
            for id_,errors in errors_data.items():
                for error in errors:
                    for message in error.messages:
                        id_errorDict.setdefault(id_,[])
                        id_errorDict[id_]+=[message]

            id_errorDict=json.dumps(id_errorDict)
            form=PostForm(None)
            return render(request,'blog\createpost.html',{'form':form,'errors':id_errorDict})
