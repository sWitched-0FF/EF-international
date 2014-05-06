# coding: utf-8
import datetime

from django.db import models


class VacationQuerySet(models.query.QuerySet):
    def on_vacation_users(self):
        return self.filter( start_date__lte=datetime.date.today(),
                            end_date__gte=datetime.date.today())


class VacationManager(models.Manager):
    def get_queryset(self):
        return VacationQuerySet(self.model, using=self._db)

    def on_vacation_users(self):
        return self.get_queryset().on_vacation_users()