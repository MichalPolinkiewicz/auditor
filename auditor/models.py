from django.db import models
from django.db.models import DateTimeField


class Target(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    cmp_class_name = models.CharField(max_length=100)
    cmp_class_xpath = models.CharField(max_length=100)
    cmp_allow_button_name = models.CharField(max_length=100)
    cmp_allow_button_xpath = models.CharField(max_length=100)

    def __str__(self):
        return self.url


class AuditResult(models.Model):
    date = DateTimeField


