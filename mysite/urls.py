from django.conf.urls import patterns, include, url
from registration.forms import RegistrationFormUniqueEmail
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^article/', include('article.urls', namespace="article")),
    url(r'^register/$', 'registration.backends.simple.views.RegistrationView', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^profile/', include('accounts.urls')),
)
