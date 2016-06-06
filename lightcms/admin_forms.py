from django import forms
from django.contrib.contenttypes.models import ContentType
from lightcms.applications_pool import applications_pool
from lightcms.models import Page


class PageAdminForm(forms.ModelForm):

    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(app_label__in=map(lambda x: x.app, applications_pool.apps.values())),
        required=False
    )

    class Meta:
        model = Page
        fields = ('parent', 'title', 'slug', 'content_type')
