from django.contrib import admin

from embed_video.admin import AdminVideoMixin

from main.admin import PageAdmin

from .models import ImageGallery, VideoGallery, DocsGallery
from .models import Image, Video, DocFile


admin.site.register(ImageGallery, PageAdmin)
admin.site.register(VideoGallery, PageAdmin)
admin.site.register(DocsGallery, PageAdmin)
admin.site.register(Image)
admin.site.register(Video)

class DocFileAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(DocFile, DocFileAdmin)