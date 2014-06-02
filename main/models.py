# coding: utf-8
import datetime

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from ckeditor.fields import RichTextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from .managers import VacationManager


class Vacation(models.Model):
    objects = VacationManager()
    start_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(default=datetime.date.today())
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name_plural = verbose_name = u'Отпуск'

class CompanyStructure(MPTTModel):
    u''' Оргструктура '''
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')
    order = models.PositiveIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ('order',)

    def save(self, *args, **kwargs):
        super(CompanyStructure, self).save(*args, **kwargs)
        CompanyStructure.objects.rebuild()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'Структура компании'


class AbstractPage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = RichTextField()
    title = models.CharField(u'Заголовок', max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(u'Актуально', default=True)
    is_publish = models.BooleanField(u'Опубликовано', default=True)

    class Meta:
        ordering = ('-created','title','user')
        abstract = True

    def __unicode__(self):
        return self.title + u' ' + unicode(self.created)


class News(AbstractPage):
    u''' Новости портала '''
    class Meta:
        verbose_name=u'Новость'
        verbose_name_plural = u'Новости'

    class Meta:
        ordering = ('-created','title','user')
        
    def get_absolute_url(self):
        return reverse('main:news', kwargs=dict(pk=self.pk))

    @classmethod
    def list_url(cls):
        return reverse('main:news_list')


class Ad(AbstractPage):
    u''' Доска Объявлений портала '''
    class Meta:
        verbose_name=u'Объявление'
        verbose_name_plural = u'Объявления'

    def get_absolute_url(self):
        return reverse('main:ads', kwargs=dict(pk=self.pk))

    @classmethod
    def list_url(cls):
        return reverse('main:ads_list')


class Contest(AbstractPage):
    u'''конкурсы '''
    class Meta:
        verbose_name=u'Конкурс'
        verbose_name_plural = u'Конкурсы'

    def get_absolute_url(self):
        return reverse('main:contests', kwargs=dict(pk=self.pk))

    @classmethod
    def list_url(cls):
        return reverse('main:contests_list')


class Calendar(AbstractPage):
    u''' календарь событий '''
    start_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(default=datetime.date.today())

    class Meta:
        verbose_name=u'Событие календаря'
        verbose_name_plural = u'Календарь событий'

    def get_absolute_url(self):
        return reverse('main:calendar_event', kwargs=dict(pk=self.pk))

    @classmethod
    def list_url(cls):
        return reverse('main:calendar')