from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']

admin.site.register(UserProfile, UserProfileAdmin)
