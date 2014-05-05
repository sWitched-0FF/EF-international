from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^company_life/$', 'company_life', name='company_life'),
    url(r'^info/$', 'info', name='info'),
    url(r'^news/$', 'news_list', name='news_list'),
    url(r'^news/(?P<pk>\d+)/$', 'news', name='news'),
    url(r'^staff/$', 'staff', name='staff'),
    url(r'^ads/(?P<pk>\d+)/$', 'ads', name='ads'),
    url(r'^contests/(?P<pk>\d+)/$', 'contests', name='contests'),
)