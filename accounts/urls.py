from django.conf.urls import patterns, include, url
from accounts import views

urlpatterns = patterns('',
	url(r'^$', views.ListUser.as_view(), name='index'),
	url(r'^edit/(?P<slug>\w+)/$', views.ViewAccount.as_view(), name='edit'),
	#url(r'^edit/(?P<slug>\w+)/$', views.MyAccount.as_view(), name='edit'),
	#url(r'^(?P<slug>\w+)/tag/$', views.forTag, name='tag'),
	#url(r'^(?P<slug>\w+)/catigory/$', views.forCategories, name='categories'),
)
