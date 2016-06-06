from django.conf.urls import url
from lightcms import views

SLUG_REGEXP = '[0-9A-Za-z-_.//]+'

regexp = r'^(?P<slug>%s)/$' % SLUG_REGEXP

urlpatterns = [
    url(regexp, views.show_page, name='show-page-by-slug'),
    url(r'^$', views.show_page, {'slug': ''}, name='pages-root'),
]
