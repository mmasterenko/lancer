# -*- coding: utf-8 -*-
from django.db import models


class SEOFieldsMixin(models.Model):
    class Meta:
        abstract = True

    title = models.CharField('<title>', max_length=100, null=True, blank=True)
    meta_desc = models.CharField('meta description', max_length=100, null=True, blank=True)
    meta_keywords = models.CharField('meta keywords', max_length=100, null=True, blank=True)
