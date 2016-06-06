
class ApplicationsPool:

    def __init__(self):
        self.apps = {}

    def register(self, app):

        if app.__name__ in self.apps:
            raise Exception(
                'A CMS application %r is already registered' % app.__name__)

        self.apps[app.__name__] = app()

applications_pool = ApplicationsPool()
