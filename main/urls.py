from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^news/(?P<pk>\d+)/$', 'news', name='news'),
    url(r'^ads/(?P<pk>\d+)/$', 'ads', name='ads'),
    url(r'^contests/(?P<pk>\d+)/$', 'contests', name='contests'),
)