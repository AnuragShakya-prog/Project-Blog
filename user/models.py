from django.db import models
from django.contrib.auth.models import User
# from .models import UserCategory
# Create your models here.


class UserCategory(models.Model):
    category=models.CharField(max_length=200)

    def __str__(self):
        return self.category


class UserProfile(models.Model):
    # def get_default_category():
    #     return UserCategory.objects.get(category="Unknown")
    username=models.CharField(max_length=100,default="")
    category=models.ForeignKey(UserCategory,on_delete=models.CASCADE,default=1)
    profile_pic=models.ImageField(upload_to="user/profile_pics/")
    date_of_birth=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

  