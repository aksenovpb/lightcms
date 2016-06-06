from django.conf import settings


class ModulesPool:

    def __init__(self):
        self.modules = set()
        self.modules.update(settings.LIGHTCMS_MODULES)

    def register(self, module):
        self.modules.add(module)

modules_pool = ModulesPool()
