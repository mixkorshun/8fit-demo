from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import InlinePanel, FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page, Orderable


class LandingPage(Page):
    offer = models.ForeignKey('plans.Offer', models.PROTECT,
                              related_name='landings',
                              verbose_name=_('offer'))

    allow_signup = models.BooleanField(default=True,
                                       verbose_name=_('allow signup'))

    parent_page_types = ['staticpages.HomePage']
    subpage_types = []

    content_panels = Page.content_panels + [
        InlinePanel('blocks', heading=_('blocks')),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('allow_signup'),
        FieldPanel('offer'),
    ]

    class Meta:
        verbose_name = _('landing page')
        verbose_name_plural = _('landing pages')


class PageBlock(models.Model):
    heading = models.CharField(max_length=255, verbose_name=_('heading'))
    content = RichTextField(verbose_name=_('content'))

    class Meta:
        abstract = True


class LandingPageBlock(Orderable, PageBlock):
    page = ParentalKey(LandingPage, on_delete=models.CASCADE,
                       related_name='blocks', verbose_name=_('page'))
