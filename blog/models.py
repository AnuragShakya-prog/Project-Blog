from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class BlogPost(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="post/images")
    pubdate=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_text=models.TextField()
    date_time=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    main_post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)