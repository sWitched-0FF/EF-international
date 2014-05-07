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


class UserManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def new_users(self):
        return self.get_queryset().new_users()

    def birthday_users(self):
        return self.get_queryset().birthday_users()

class User(AbstractUser):
    objects = UserManager()
    date_of_birth = models.DateField(null=True)
    post = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    USERNAME_FIELD = 'username'