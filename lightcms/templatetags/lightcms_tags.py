from importlib import import_module
from classytags.arguments import Argument
from classytags.core import Options
from classytags.utils import flatten_context
from django import template
from sekizai.templatetags.sekizai_tags import RenderBlock, SekizaiParser

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()


class LightCmsToolbar(RenderBlock):
    name = 'lightcms_toolbar'

    options = Options(
        Argument('name', required=False),  # just here so sekizai thinks this is a RenderBlock
        parser_class=SekizaiParser,
    )

    def render_tag(self, context, name, nodelist):
        # render JS
        rendered_contents = nodelist.render(context)
        toolbar = render_to_string('lightcms/toolbar/toolbar.html', flatten_context(context))
        # return the toolbar content and the content below
        return '%s\n%s' % (toolbar, rendered_contents)

register.tag(LightCmsToolbar)


class LightCmsRenderBlock(RenderBlock):
    name = 'light_cms_render_block'

    options = Options(
        Argument('name', required=False),  # just here so sekizai thinks this is a RenderBlock
        parser_class=SekizaiParser,
    )

    def render_tag(self, context, name, nodelist):
        rendered_contents = nodelist.render(context)
        items = []
        modules = ''
        for item in context:
            if 'modules_on_pages' in item:
                block = self.token.split_contents()[1]
                items = filter(lambda x: x[0] == block, item['modules_on_pages'])
        for item in items:
            struct = item[1].split('.')
            load_class = struct.pop()
            module = import_module('.'.join(struct))
            modules += getattr(module, load_class)().render()
        # module = import_module('articles.modules')
        # print getattr(module, 'List')().render()
        # return the toolbar content and the content below
        return '%s\n%s' % (modules, rendered_contents)

register.tag(LightCmsRenderBlock)
