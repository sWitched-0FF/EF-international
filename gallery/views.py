#coding: utf-8
from main.views import DetailPage, IndexPage

from .models import ImageGallery, VideoGallery, DocsGallery
#from .models import Image, Video, DocFile


image_gallery_list = IndexPage.as_view(template_name='news_list.html')
video_gallery_list = IndexPage.as_view(template_name='news_list.html')
docs_gallery_list = IndexPage.as_view(template_name='news_list.html')

image_gallery = DetailPage.as_view( model=ImageGallery,
                                    template_name='image_gallery.html')
video_gallery = DetailPage.as_view( model=VideoGallery,
                                    template_name='video_gallery.html')
docs_gallery = DetailPage.as_view(  model=DocsGallery,
                                    template_name='docs_gallery.html')