from django.forms import ModelForm
from user.models import UserProfile

class ProfilePicForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=['username','category','profile_pic','date_of_birth']
        