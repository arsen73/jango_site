from django.conf.urls import patterns, include, url
from article import views

urlpatterns = patterns('',
	url(r'^$', views.ListArticlesView.as_view(), name='index'),
	#url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	#url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	#url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
