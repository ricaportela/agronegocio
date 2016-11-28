""" Models """
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .choices import MEASUREMENT_UNIT


class Product(models.Model):
    """ Product """
    description = models.CharField(max_length=50, null=True)
    quantitystock = models.IntegerField()
    unitmeasurement = models.CharField(
        _('Unidade'), max_length=2, blank=True, choices=MEASUREMENT_UNIT
    )
    unitprice = models.FloatField()
    averageprice = models.FloatField()
    lastupdate = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.description

    class Meta:
        """ Meta Class Product """
        ordering = ["description"]


class HarvestTime(models.Model):
    """ Harvest Time """
    description = models.CharField(max_length=50, null=True)
    begindate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return self.description


