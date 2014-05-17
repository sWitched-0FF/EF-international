#coding: utf-8
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from filer.fields.image import FilerImageField
from embed_video.fields import EmbedVideoField

from main.models import AbstractPage


class ImageGallery(AbstractPage):
    class Meta:
        verbose_name=u'Галерея изображений'
        verbose_name_plural = u'Галереи изображений'

    def get_absolute_url(self):
        return reverse('gallery:image_gallery', kwargs=dict(pk=self.pk))    


class VideoGallery(AbstractPage):
    class Meta:
        verbose_name=u'Галерея видео'
        verbose_name_plural = u'Галереи видео'

    def get_absolute_url(self):
        return reverse('gallery:video_gallery', kwargs=dict(pk=self.pk))  


class DocsGallery(AbstractPage):
    class Meta:
        verbose_name=u'Галерея документов'
        verbose_name_plural = u'Галереи документов'

    def get_absolute_url(self):
        return reverse('gallery:docs_gallery', kwargs=dict(pk=self.pk))  


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    gallery = models.ForeignKey(ImageGallery, verbose_name=u'Галерея', null=True)
    image = FilerImageField()

    def __unicode__(self):
        name = self.image.name or self.image.original_filename
        if self.gallery:
            return self.gallery.title + u' ' + name

    class Meta:
        verbose_name=u'изображение'
        verbose_name_plural = u'изображения'

    def get_absolute_url(self):
        return reverse('gallery:image', kwargs=dict(pk=self.pk))


class Video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    gallery = models.ForeignKey(VideoGallery, verbose_name=u'Галерея', null=True)
    video = EmbedVideoField()

    def __unicode__(self):
        name = self.video
        if self.gallery:
            return self.gallery.title + u' ' + name

    class Meta:
        verbose_name=u'видео'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('gallery:video', kwargs=dict(pk=self.pk))


class DocFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    gallery = models.ForeignKey(DocsGallery, verbose_name=u'Галерея', null=True)
    doc_file = models.FileField(upload_to='docs/')

    def __unicode__(self):
        name = self.doc_file.name
        if self.gallery:
            return self.gallery.title + u' ' + name

    class Meta:
        verbose_name=u'документ'
        verbose_name_plural = u'документы'

    def get_absolute_url(self):
        return reverse('gallery:doc_file', kwargs=dict(pk=self.pk))