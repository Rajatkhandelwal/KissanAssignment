import calendar
from datetime import datetime

from django.db import models
from django.utils import timezone
from .regionConstant import AreaList

class MetricsBaseManager(models.Manager):

    def add_or_update_record(self, value, region, month, year):
        try:
            # func_tag = "MetricsBaseManager:add_record"
            day = calendar.monthrange(year, month)[1]
            dt = timezone.datetime(year, month, day)
            return self.update_or_create(record_date=dt,
                                         region=region,
                                         defaults={"value": value})

        except Exception as exc:
            raise exc



class MetricsBase(models.Model):
    value = models.FloatField(default=0.0)
    region = models.CharField(max_length=8, choices=AreaList)
    record_date = models.DateField()

    objects = MetricsBaseManager()
    class Meta:
        abstract = True
        ordering = ["record_date"]

    @property
    def year(self):
        return self.record_date.year

    @property
    def month(self):
        return self.record_date.month


class MaxTemperature(MetricsBase):
    UNIT = "DegC"

    def __str__(self):
        return "Tmax <%s:%s %s> (%s)" % (self.region, self.value, self.UNIT, self.record_date)


class MinTemperature(MetricsBase):
    UNIT = "DegC"

    def __str__(self):
        return "Tmin <%s:%s %s> (%s)" % (self.region, self.value, self.UNIT, self.record_date)


class Rainfall(MetricsBase):
    UNIT = "mm"

    def __str__(self):
        return "Rainfall <%s:%s %s> (%s)" % (self.region, self.value, self.UNIT, self.record_date)
