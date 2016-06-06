import os
from importlib import import_module
from xml.etree import ElementTree

from django.conf import settings
from lightcms.blocks_pool import blocks_pool

from lightcms.modules_pool import modules_pool

for app in settings.INSTALLED_APPS:
    try:
        import_module(app + '.cms_app')
    except ImportError:
        pass

tree = ElementTree.parse(os.path.join(settings.BASE_DIR, 'lightcms/templates/lightcms/template.xml'))
for child in tree.getroot():
    blocks_pool.register(child.text)
