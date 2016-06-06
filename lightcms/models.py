from __future__ import unicode_literals
from django.contrib.contenttypes.models import ContentType

from django.db import models
import mptt
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Page(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name="Pages")

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    content_type = models.ForeignKey(ContentType, null=True)

    def __unicode__(self):
        return u'%s' % self.title

mptt.register(Page)


class Block(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        unique_together = ('title', )

    def __unicode__(self):
        return u'%s' % self.title


class Module(models.Model):
    path = models.CharField(max_length=255)

    class Meta:
        unique_together = ('path', )

    def __unicode__(self):
        return u'%s' % self.path


class ModuleRelation(models.Model):
    module = models.ForeignKey(Module)
    blocks = models.ManyToManyField(Block)
    pages = models.ManyToManyField(Page)

    def __unicode__(self):
        return u'%s' % self.module
