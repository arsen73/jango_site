from django.conf.urls import patterns, include, url
from article import views

urlpatterns = patterns('',
	url(r'^$', views.ListArticlesView.as_view(), name='index'),
	url(r'^(?P<slug>\w+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<slug>\w+)/tag/$', views.forTag, name='tag'),
	url(r'^(?P<slug>\w+)/catigory/$', views.forCategories, name='categories'),
	#url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	#url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
