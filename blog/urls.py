from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls import static


#Url mapping are here
urlpatterns = [
    path('',views.home,name="home"),
    path('post/<int:id>/',views.postView,name='postView'),
    path('profile',views.profile_view,name='profile'),
    path('createpost',views.create_post,name='create_post'),
]