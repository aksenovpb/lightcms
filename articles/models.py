from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return u'%s' % self.title
