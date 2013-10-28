# coding: utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from accounts.models import UserProfile, Team
from django.contrib.auth.models import User
from django.views import generic
from django.utils import timezone

class ViewAccount(generic.DetailView):
	model = UserProfile
	template_name = "accounts/edit.html"
	context_object_name = "account"


class ListUser(generic.ListView):
	model = UserProfile
	template_name = "accounts/users.html"
	context_object_name = "user"

	def get_queryset(self):
		content = UserProfile.objects.all()
		return content

def forTag(request,slug):
	article_list = Articles.objects.filter(tagList=TagArticles.objects.filter(slug=slug)).order_by('-date_publish')[:5]
	tag = TagArticles.objects.filter(slug=slug)[:1]
	return render(request, 'article/list.html', {'article_list': article_list, 'breadcrumbs': tag[0]})