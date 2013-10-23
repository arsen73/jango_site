# coding: utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from article.models import UserProfile, Team
from django.views import generic
from django.utils import timezone

class MyAccount(Object):
	template_name = "article/list.html"
	context_object_name = "article_list"

	def Form(self):
		content = Articles.objects.filter(date_publish__lte=timezone.now()).order_by('-date_publish')[:5]
		return content

class DetailView(generic.DetailView):
	model = Articles
	template_name = "article/detail.html"
	context_object_name = "article"

def forTag(request,slug):
	article_list = Articles.objects.filter(tagList=TagArticles.objects.filter(slug=slug)).order_by('-date_publish')[:5]
	tag = TagArticles.objects.filter(slug=slug)[:1]
	return render(request, 'article/list.html', {'article_list': article_list, 'breadcrumbs': tag[0]})