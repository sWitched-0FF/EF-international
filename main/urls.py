from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),

    url(r'^ads/$', 'ads_list', name='ads_list'),
    url(r'^ads/(?P<pk>\d+)/$', 'ads', name='ads'),
    url(r'^calendar/$', 'calendar', name='calendar'),
    url(r'^calendar/(?P<pk>\d+)/$', 'calendar_event', name='calendar_event'),
    url(r'^company_life/$', 'company_life', name='company_life'),
    url(r'^contests/$', 'contests_list', name='contests_list'),
    url(r'^contests/(?P<pk>\d+)/$', 'contests', name='contests'),
    url(r'^info/$', 'info', name='info'),
    url(r'^news/$', 'news_list', name='news_list'),
    url(r'^news/(?P<pk>\d+)/$', 'news', name='news'),
    url(r'^staff/$', 'staff', name='staff'),
)