# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand

from lightcms import modules_pool
from lightcms.models import Module


class Command(BaseCommand):

    def handle(self, *args, **options):
        for module_path in modules_pool.modules:
            Module.objects.get_or_create(path=module_path)
