from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ZooKeeper.views',
url(r'^admin/', include(admin.site.urls) ),
url(r'^$', 'index'),
url(r'^index/?$', 'index'),
url(r'^contact/?$', 'contact'),
url(r'^about/?$', 'about'),
url(r'^blog/?$', 'blog'),
)

