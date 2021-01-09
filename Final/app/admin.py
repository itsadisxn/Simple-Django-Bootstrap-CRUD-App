from django.contrib import admin
from .models import User, Profile


""" """
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'profile_type', 'location')
    list_filter = ('profile_type', 'location')
    pass

admin.site.register(Profile, ProfileAdmin)