from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^ckeditor/', include('ckeditor.urls')),

    url(r'^$', 'main.views.index', name='index'),
    url(r'', include('main.urls', namespace='main')),
    url(r'gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.login', name='login')
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)