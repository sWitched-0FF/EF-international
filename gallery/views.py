#coding: utf-8
from main.views import DetailPage, ListPage

from .models import ImageGallery, VideoGallery, DocsGallery


image_gallery_list = ListPage.as_view(model=ImageGallery)
video_gallery_list = ListPage.as_view(model=VideoGallery)
docs_gallery_list = ListPage.as_view(model=DocsGallery)

image_gallery = DetailPage.as_view( model=ImageGallery,
                                    template_name='image_gallery.html')
video_gallery = DetailPage.as_view( model=VideoGallery,
                                    template_name='video_gallery.html')
docs_gallery = DetailPage.as_view(  model=DocsGallery,
                                    template_name='docs_gallery.html')