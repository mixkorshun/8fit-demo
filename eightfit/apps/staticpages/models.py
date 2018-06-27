from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page


class HomePage(Page):
    body = RichTextField(blank=True, verbose_name=_('body'))

    parent_page_types = ['wagtailcore.Page']

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = _('home page')
        verbose_name_plural = _('home pages')


class StaticPage(Page):
    body = RichTextField(blank=True, verbose_name=_('body'))

    parent_page_types = [
        'staticpages.HomePage',
        'staticpages.StaticPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = _('static page')
        verbose_name_plural = _('static pages')
