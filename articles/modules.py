from django.template.loader import render_to_string
from articles.models import Article


class List:
    template = 'articles/list.html'

    def render(self):
        objs = self.get_queryset()
        return render_to_string(self.template, {'objs': objs})

    def get_queryset(self, **kwargs):
        return Article.objects.filter(**kwargs)


class Detail:
    template = 'articles/detail.html'

    def render(self):
        obj = self.get_queryset()
        return render_to_string(self.template, {'obj': obj})

    def get_queryset(self, **kwargs):
        return Article.objects.filter(**kwargs)[0]
