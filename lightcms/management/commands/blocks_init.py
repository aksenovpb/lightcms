# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand

from lightcms import blocks_pool
from lightcms.models import Block


class Command(BaseCommand):

    def handle(self, *args, **options):
        for block_title in blocks_pool.blocks:
            Block.objects.get_or_create(title=block_title)
