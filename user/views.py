from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
import json
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfilePicForm
import blog.views as blog_views
# Create your views here.


add_user_profile=blog_views.add_user_profile
def register(request):
    if request.method=="GET":
        form=UserCreationForm(None)
    
        return render(request,'user\\register.html',{'form':form})
    else:
        request.POST['user']=request.user
        form=UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.add_message(request,messages.SUCCESS,f"User {username} successfully created")
            print(f"User {username} created")
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
            form=UserCreationForm(None)
            return render(request,'user\\register.html',{'form':form,'errors':id_errorDict})
            


def profile_update(request):
    user=request.user
    if request.method=='GET':
        try:
            user_profile=UserProfile.objects.get(user=user)
            profile_form=ProfilePicForm(instance=user_profile)
            context={"form":profile_form}
            context=add_user_profile(request,context)
            return render(request,"user/profileupdate.html",context)
        except ObjectDoesNotExist as ode:
            profile_form=ProfilePicForm()
            return render(request,"user/profileupdate.html",{"form":profile_form})

    elif request.method=='POST':
        # post_data=dict(request.POST)+{'user':request.user}
        user=request.user
        try:
            user_profile=UserProfile.objects.get(user=user)
            form=ProfilePicForm(request.POST,request.FILES,instance=user_profile)
        except ObjectDoesNotExist as objdoe:
            form=ProfilePicForm(request.POST,request.FILES)
        if form.is_valid():
            new_profile=form.save(commit=False)
            new_profile.user=request.user
            new_profile.save()
        else:
            errors_data=dict(form.errors.as_data())
            id_errorDict={}
            for id_,errors in errors_data.items():
                for error in errors:
                    for message in error.messages:
                        id_errorDict.setdefault(id_,[])
                        id_errorDict[id_]+=[message]

            id_errorDict=json.dumps(id_errorDict)
            form=ProfilePicForm(None)
            return render(request,'user\\profileupdate.html',{'form':form,'errors':id_errorDict})
        return redirect('/')
    

