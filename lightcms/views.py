from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from lightcms.applications_pool import applications_pool
from lightcms.models import Page, ModuleRelation


def get_page_by_slug(slug):
    slugs = slug.split('/')
    slugs.reverse()

    where = {}
    prefix = 'parent__'
    field = 'slug'
    for slug in slugs:
        where.update({field: slug})
        field = prefix + field

    print slugs
    print slugs
    print slugs
    if slugs[0] == '':
        where = {'level': 0}
    return get_object_or_404(Page, **where)


def show_page(request, slug):
    page = get_page_by_slug(slug)

    application_module = ()
    if page.content_type:
        application_module = [('content', page.content_type.app_label + '.modules.List')]
    elif page.parent.content_type:
        application_module = [('content', page.parent.content_type.app_label + '.modules.Detail')]

    page_modules = ModuleRelation.objects.filter(pages=page).values_list('blocks__title', 'module__path')

    return TemplateResponse(request, 'lightcms/base.html', {
        'page': page.title,
        'modules_on_pages': application_module + list(page_modules)
    })
