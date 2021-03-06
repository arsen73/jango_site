# coding: utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from accounts.models import UserProfile, Team
from django.contrib.auth.models import User
from django.views import generic
from django.utils import timezone
from forms import UserProfileForm

class ViewAccount(generic.DetailView):
	model = UserProfile
	template_name = "accounts/view.html"
	context_object_name = "account"


class ListUser(generic.ListView):
	model = UserProfile
	template_name = "accounts/users.html"
	context_object_name = "users"

	def get_queryset(self):
		content = UserProfile.objects.all()
		return content

def MyAccount(request, slug):
	if not request.user.is_authenticated():
		return redirect('/accounts/login')
	profile = UserProfile.objects.get(slug = slug)
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			profile = UserProfile.objects.get(slug = slug)
			form = UserProfileForm(instance=profile)
		return render(request, 'accounts/edit.html', {'form': form})
	form = UserProfileForm(instance=profile)
	return render(request, 'accounts/edit.html', {'form': form})