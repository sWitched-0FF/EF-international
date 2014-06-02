# coding: utf-8
import datetime

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserQuerySet(models.query.QuerySet):
    start_date = datetime.date.today() - datetime.timedelta(days=7)
    end_date = datetime.date.today() + datetime.timedelta(days=7)

    def new_users(self):
        return self.filter(date_joined__gte=self.start_date)

    def birthday_users(self):
        return self.filter( date_of_birth__isnull=False,
                            date_of_birth__gte=self.start_date,
                            date_of_birth__lte=self.end_date,)

    def with_phones(self):
        return self.filter(phone__isnull=False
                  ).exclude(phone__exact='')


class UserManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def new_users(self):
        return self.get_queryset().new_users()

    def birthday_users(self):
        return self.get_queryset().birthday_users()

    def with_phones(self):
        return self.get_queryset().with_phones()

class User(AbstractUser):
    objects = UserManager()
    date_of_birth = models.DateField(null=True)
    post = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    USERNAME_FIELD = 'username'

    def get_full_name(self):
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        if self.post:
            full_name = '{0} {1}'.format(full_name, self.post)
        return full_name.strip() or self.username