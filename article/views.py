# coding: utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from article.models import Articles, TagArticles
from django.views import generic
from django.utils import timezone

class ListArticlesView(generic.ListView):
	template_name = "article/list.html"
	context_object_name = "article_list"

	def get_queryset(self):
		content = Articles.objects.filter(date_publish__lte=timezone.now()).order_by('-date_publish')[:5]
		return content

class DetailView(generic.DetailView):
	model = Articles
	template_name = "article/detail.html"
	context_object_name = "article"

class ArticlesForTag(generic.ListView):
	model = Articles
	template_name = "article/list.html"
	context_object_name = "article_list"

	def get_queryset(self):
		content = Articles.objects.filter(tagList=slug).order_by('-date_publish')[:5]
		return content

class ArticlesForCategories(generic.ListView):
	model = Articles
	template_name = "article/list.html"
	context_object_name = "article_list"		