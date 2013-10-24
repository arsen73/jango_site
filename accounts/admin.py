# coding: utf8
from .models import UserProfile, Team
from django.contrib import admin


class CustomerUserProfile(admin.ModelAdmin):
	list_display = ('user', 'gender', 'date_birth',)
	list_filter = ('user', 'gender', 'date_birth',)
admin.site.register(UserProfile, CustomerUserProfile)

admin.site.register(Team)