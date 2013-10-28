#! coding: utf-8

from models import UserProfile
from django.contrib.auth.models import User

def context(request):
    user_info = UserProfile.objects.filter(user=request.user.id)
    return {'user_info': user_info[0]}