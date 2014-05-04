# coding: utf-8
import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models

from ckeditor.fields import RichTextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Vacation(models.Model):
    start_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(default=datetime.date.today())
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = verbose_name = u'Отпуск'

class CompanyStructure(MPTTModel):
    u''' Оргструктура '''
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')
    order = models.PositiveIntegerField()

    class MPTTMeta:
        order_insertion_by = ('order',)

    def save(self, *args, **kwargs):
        super(CompanyStructure, self).save(*args, **kwargs)
        CompanyStructure.objects.rebuild()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'Структура компании'


class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    post = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    department = models.ForeignKey(CompanyStructure, null=True)
    vacation = models.ManyToManyField(Vacation, null=True)
    USERNAME_FIELD = 'username'


class AbstractPage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = RichTextField()
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_publish = models.BooleanField(default=True)

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

    def get_absolute_url(self):
        return reverse('main:news', kwargs=dict(pk=self.pk))


class Ad(AbstractPage):
    u''' Доска Объявлений портала '''
    class Meta:
        verbose_name=u'Объявление'
        verbose_name_plural = u'Объявления'

    def get_absolute_url(self):
        return reverse('main:ads', kwargs=dict(pk=self.pk))


class Contest(AbstractPage):
    u'''конкурсы '''
    class Meta:
        verbose_name=u'Конкурс'
        verbose_name_plural = u'Конкурсы'

    def get_absolute_url(self):
        return reverse('main:contests', kwargs=dict(pk=self.pk))