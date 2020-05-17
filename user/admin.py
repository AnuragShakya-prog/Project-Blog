from django.contrib import admin
from .models import UserProfile,UserCategory
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserCategory)