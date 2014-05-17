from django.conf.urls import patterns, url

urlpatterns = patterns('gallery.views',
    url(r'^image_gallery_list/$', 'image_gallery_list', name='image_gallery_list'),
    url(r'^image_gallery/(?P<pk>\d+)/$', 'image_gallery', name='image_gallery'),
    url(r'^video_gallery_list/$', 'video_gallery_list', name='video_gallery_list'),
    url(r'^video_gallery/(?P<pk>\d+)/$', 'video_gallery', name='video_gallery'),
    url(r'^docs_gallery_list/$', 'docs_gallery_list', name='docs_gallery_list'),
    url(r'^docs_gallery/(?P<pk>\d+)/$', 'docs_gallery', name='docs_gallery'),
)